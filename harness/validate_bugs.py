"""Quality check of the bug set (run before any model experiment).

For every bug it must hold that:
  1. buggy.py FAILS the visible tests  (the bug is observable by the feedback signal)
  2. buggy.py FAILS overall             (visible + hidden)
  3. fixed.py PASSES visible and hidden (the tests are satisfiable and correct)
Writes results/validation.csv and exits with code 1 if any bug is invalid.
"""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from run_tests import evaluate  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    rows, bad = [], 0
    for bid in sorted(os.listdir(os.path.join(ROOT, "bugs"))):
        d = os.path.join(ROOT, "bugs", bid)
        meta = json.load(open(os.path.join(d, "meta.json")))
        b = evaluate(open(os.path.join(d, "buggy.py")).read(), d)
        f = evaluate(open(os.path.join(d, "fixed.py")).read(), d)
        valid = (b["visible"]["status"] != "pass" and not b["fixed"] and f["fixed"])
        bad += not valid
        rows.append({"bug_id": bid, "category": meta["category"], "subtype": meta["subtype"],
                     "buggy_visible": b["visible"]["status"], "buggy_hidden": b["hidden"]["status"],
                     "fixed_visible": f["visible"]["status"], "fixed_hidden": f["hidden"]["status"],
                     "n_tests": f["visible"]["n_run"] + f["hidden"]["n_run"],
                     "valid": valid})
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    out = os.path.join(ROOT, "results", "validation.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['bug_id']}  {r['category']:9s} buggy: vis={r['buggy_visible']:13s} "
              f"hid={r['buggy_hidden']:13s} | fixed: vis={r['fixed_visible']} "
              f"hid={r['fixed_hidden']}  tests={r['n_tests']}  {'OK' if r['valid'] else 'INVALID'}")
    print(f"\n{len(rows) - bad}/{len(rows)} bugs valid -> {out}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
