"""Runs the debugging experiment.

Conditions (same bugs, same model, same prompt wording):
  zero_shot  - one attempt, no feedback.
  iterative  - up to MAX_TURNS attempts; after each attempt that fails the VISIBLE tests,
               the visible test output is sent back to the model as feedback.
  sampled    - control: MAX_TURNS independent zero-shot attempts (higher temperature),
               no feedback; the first one that passes the visible tests is kept.
               Same attempt budget as `iterative`, so any gain of iterative over sampled
               can be attributed to the feedback content, not to extra attempts.

A bug counts as fixed only if the final patch passes the visible AND hidden tests.
Hidden tests are never shown to the model.

Usage:
  python harness/experiment.py --config config.json --out results/run1
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
from llm_client import make_client          # noqa: E402
from prompts import SYSTEM, ZERO_SHOT, FEEDBACK, extract_code  # noqa: E402
from run_tests import evaluate, run_suite    # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_bugs(bug_ids=None):
    bugs = []
    for bid in sorted(os.listdir(os.path.join(ROOT, "bugs"))):
        d = os.path.join(ROOT, "bugs", bid)
        if bug_ids and bid not in bug_ids:
            continue
        with open(os.path.join(d, "meta.json")) as f:
            meta = json.load(f)
        with open(os.path.join(d, "buggy.py")) as f:
            meta["buggy_code"] = f.read()
        meta["dir"] = d
        bugs.append(meta)
    return bugs


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()[:12]


class Logger:
    def __init__(self, out_dir):
        os.makedirs(out_dir, exist_ok=True)
        self.attempts = open(os.path.join(out_dir, "attempts.jsonl"), "a")
        self.results = open(os.path.join(out_dir, "results.jsonl"), "a")

    def attempt(self, rec):
        self.attempts.write(json.dumps(rec) + "\n")
        self.attempts.flush()

    def result(self, rec):
        self.results.write(json.dumps(rec) + "\n")
        self.results.flush()


def one_attempt(client, messages, bug, temperature=None):
    t0 = time.time()
    try:
        response = client.chat(messages, temperature=temperature)
        api_error = None
    except Exception as exc:  # network / server problems are logged, not hidden
        response, api_error = "", repr(exc)
    latency = round(time.time() - t0, 2)
    code = extract_code(response)
    if code is None:
        ev = {"visible": {"status": "no_code", "output": "No ```python code block found."},
              "hidden": {"status": "no_code"}, "fixed": False}
    else:
        ev = evaluate(code, bug["dir"])
    return response, code, ev, latency, api_error


def failure_type(ev):
    if ev["fixed"]:
        return "fixed"
    v, h = ev["visible"]["status"], ev["hidden"]["status"]
    if v in ("no_code", "syntax_error", "timeout"):
        return v
    if v == "pass" and h != "pass":
        return "overfit_visible"  # passes the tests it saw, fails the hidden ones
    return "tests_fail"


def run_condition(client, bug, condition, max_turns, sample_temp, log, run_meta):
    if hasattr(client, "start_bug"):
        client.start_bug(bug["dir"])
    first_msgs = [{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": ZERO_SHOT.format(code=bug["buggy_code"])}]
    turns = 1 if condition == "zero_shot" else max_turns
    messages = list(first_msgs)
    final_ev, used = None, 0
    for turn in range(1, turns + 1):
        if condition == "sampled":
            if hasattr(client, "start_bug"):
                client.start_bug(bug["dir"])
            messages = list(first_msgs)
            resp, code, ev, lat, err = one_attempt(client, messages, bug, sample_temp)
        else:
            resp, code, ev, lat, err = one_attempt(client, messages, bug)
        used = turn
        log.attempt({**run_meta, "bug_id": bug["id"], "category": bug["category"],
                     "condition": condition, "turn": turn, "prompt_sha": sha(json.dumps(messages)),
                     "response": resp, "code_sha": sha(code) if code else None,
                     "visible_status": ev["visible"]["status"],
                     "hidden_status": ev["hidden"]["status"], "fixed": ev["fixed"],
                     "visible_output": ev["visible"].get("output", "")[:1500],
                     "latency_s": lat, "api_error": err})
        final_ev = ev
        if ev["visible"]["status"] == "pass":
            break  # stop rule uses only information the model/user could see
        if condition == "iterative":
            messages = messages + [
                {"role": "assistant", "content": resp},
                {"role": "user", "content": FEEDBACK.format(
                    test_output=ev["visible"].get("output", "")[-1500:])}]
    log.result({**run_meta, "bug_id": bug["id"], "category": bug["category"],
                "subtype": bug["subtype"], "condition": condition, "turns_used": used,
                "fixed": final_ev["fixed"], "failure_type": failure_type(final_ev)})
    return final_ev["fixed"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--conditions", default=None, help="comma list; default from config")
    ap.add_argument("--bugs", default=None, help="comma list of bug ids; default all")
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)
    client = make_client(cfg["model"])
    conditions = (args.conditions or ",".join(cfg["conditions"])).split(",")
    bugs = load_bugs(args.bugs.split(",") if args.bugs else None)
    run_meta = {"run_id": os.path.basename(os.path.normpath(args.out)),
                "model": client.name,
                "started": dt.datetime.now().isoformat(timespec="seconds")}
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "run_info.json"), "w") as f:
        json.dump({**run_meta, "config": cfg, "python": sys.version.split()[0],
                   "platform": platform.platform(), "n_bugs": len(bugs),
                   "conditions": conditions}, f, indent=2)
    log = Logger(args.out)
    for cond in conditions:
        for bug in bugs:
            ok = run_condition(client, bug, cond, cfg.get("max_turns", 3),
                               cfg.get("sample_temperature", 0.8), log, run_meta)
            print(f"{cond:10s} {bug['id']}  {bug['category']:9s} {'FIXED' if ok else '-'}")


if __name__ == "__main__":
    main()
