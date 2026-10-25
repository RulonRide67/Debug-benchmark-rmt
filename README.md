# LLM debugging evaluation harness (Assignment 3 – core practical component)

Evaluates one LLM on a leakage-aware set of Python bugs in four categories
(syntax, logic, runtime, security) under three conditions:

| Condition  | What the model gets | Attempts |
|------------|--------------------|----------|
| zero_shot  | buggy code + docstring | 1 |
| iterative  | same, then the output of the *visible* tests after each failed attempt | up to 3 |
| sampled    | control: 3 independent zero-shot attempts (temperature 0.8), no feedback | up to 3 |

A bug counts as **fixed** only if the final patch passes visible **and** hidden tests.
Hidden tests are never shown to the model.

## Layout
```
bugs/<ID>/buggy.py        code given to the model
bugs/<ID>/fixed.py        reference fix (never shown to the model)
bugs/<ID>/test_visible.py tests whose output is used as feedback
bugs/<ID>/test_hidden.py  held-out tests for the final verdict
bugs/<ID>/meta.json       category, subtype, origin, creation date
harness/validate_bugs.py  checks that every bug is valid (buggy fails, fix passes)
harness/experiment.py     runs the conditions and logs every attempt (JSONL)
harness/analyze.py        fix rates, Wilson CIs, McNemar, permutation test, chart
configs/                  model configurations (mock_* are pipeline tests only)
results/                  outputs
```

## Requirements
Python 3.10+ (developed with 3.13). Experiment code uses only the standard library;
`analyze.py` optionally uses scipy and matplotlib (`pip install -r requirements.txt`).

## Running the real pilot (on your own computer)
1. Install Ollama: https://ollama.com/download
2. `ollama pull qwen2.5-coder:7b`  (about 4.7 GB; needs ~8 GB RAM)
3. Check the bugs:   `python harness/validate_bugs.py`
4. Run:              `python harness/experiment.py --config configs/qwen_ollama.json --out results/pilot_qwen7b`
5. Analyse:          `python harness/analyze.py results/pilot_qwen7b`
6. Determinism check (optional): run step 4 again with `--conditions zero_shot --out results/pilot_qwen7b_rerun`
   and compare the zero-shot verdicts.

Record `ollama --version` and the model digest (`ollama show qwen2.5-coder:7b`) in the report.

## Safety
Model-generated code is executed. Each test runs in a separate process, in a temp
folder, with a 10 s timeout and a minimal environment (no API keys). For the full
study run it inside a container or VM without network access.

## Pipeline checks (no model involved)
`configs/mock_*.json` replace the model by fixed stand-ins (unchanged buggy code,
the reference fix, or "wrong first, fixed after feedback"). They prove that the
harness, logging and analysis work. **They are not model results.**
