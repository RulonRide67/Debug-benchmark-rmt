"""Runs a candidate solution against a bug's unit tests in an isolated temp directory.

Each candidate is written to solution.py next to a copy of the test file and executed
in a separate Python process with a timeout, so a crashing or hanging patch cannot
affect the harness itself.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

TIMEOUT_S = 10
MAX_OUTPUT = 3000


def _parse_unittest(output):
    ran = re.search(r"Ran (\d+) tests?", output)
    n_run = int(ran.group(1)) if ran else 0
    failures = errors = 0
    m = re.search(r"FAILED \(([^)]*)\)", output)
    if m:
        for part in m.group(1).split(","):
            k, _, v = part.strip().partition("=")
            if k == "failures":
                failures = int(v)
            elif k == "errors":
                errors = int(v)
    ok = bool(re.search(r"^OK", output, re.M)) and n_run > 0
    return n_run, failures, errors, ok


def run_suite(code, bug_dir, suite):
    """suite is 'visible' or 'hidden'. Returns a dict describing the outcome."""
    try:
        compile(code, "solution.py", "exec")
    except SyntaxError as exc:
        return {"suite": suite, "status": "syntax_error", "n_run": 0, "failures": 0,
                "errors": 1, "output": f"SyntaxError: {exc.msg} (line {exc.lineno})"}

    tmp = tempfile.mkdtemp(prefix="dbg_")
    try:
        with open(os.path.join(tmp, "solution.py"), "w") as f:
            f.write(code)
        test_file = f"test_{suite}.py"
        shutil.copy(os.path.join(bug_dir, test_file), tmp)
        # minimal environment: no API keys or other secrets are passed to model-written code
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0",
               "PYTHONDONTWRITEBYTECODE": "1"}
        for k in ("SYSTEMROOT", "TEMP", "TMP"):  # needed by Python on Windows
            if k in os.environ:
                env[k] = os.environ[k]
        try:
            proc = subprocess.run([sys.executable, "-E", "-s", test_file],
                                  cwd=tmp, env=env, capture_output=True, text=True,
                                  timeout=TIMEOUT_S)
        except subprocess.TimeoutExpired:
            return {"suite": suite, "status": "timeout", "n_run": 0, "failures": 0,
                    "errors": 1, "output": f"Timed out after {TIMEOUT_S}s"}
        output = (proc.stdout + proc.stderr)[-MAX_OUTPUT:]
        n_run, failures, errors, ok = _parse_unittest(output)
        status = "pass" if ok else ("fail" if n_run > 0 else "error")
        return {"suite": suite, "status": status, "n_run": n_run,
                "failures": failures, "errors": errors, "output": output}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def evaluate(code, bug_dir):
    """Runs both suites. A patch counts as a fix only if visible AND hidden tests pass."""
    vis = run_suite(code, bug_dir, "visible")
    hid = run_suite(code, bug_dir, "hidden")
    return {"visible": vis, "hidden": hid,
            "fixed": vis["status"] == "pass" and hid["status"] == "pass"}
