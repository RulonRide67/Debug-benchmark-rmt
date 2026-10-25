"""Analysis of results.jsonl produced by experiment.py.

Outputs (in the run folder):
  summary.md            - all tables below in Markdown
  fix_rates.csv         - fix rate per category x condition with Wilson 95% CI
  failure_types.csv     - counts of final failure types
  fix_rates.png         - grouped bar chart

Analyses:
  O2/O3: fix rate per category and condition, Wilson 95% confidence intervals.
  H1:    does the fix rate differ across categories? (chi-square on 4x2 table plus a
         permutation test, because expected counts are small)
  H2:    iterative vs zero-shot on the same bugs: exact McNemar test (paired).
  Control: iterative vs sampled (same attempt budget) - McNemar.
  Sub-question: per-category difference iterative - zero_shot.

Usage: python harness/analyze.py results/run1
"""
import csv
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict

CATS = ["syntax", "logic", "runtime", "security"]


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, centre - half), min(1.0, centre + half)


def mcnemar_exact(b, c):
    """b = A fixed & B not, c = B fixed & A not. Two-sided exact binomial p."""
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    p = sum(math.comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return min(1.0, 2 * p)


def chi2_stat(table):
    rows = [r for r in table if sum(r) > 0]
    tot = sum(map(sum, rows))
    col = [sum(r[j] for r in rows) for j in range(2)]
    if tot == 0 or 0 in col:
        return 0.0
    s = 0.0
    for r in rows:
        rt = sum(r)
        for j in range(2):
            e = rt * col[j] / tot
            s += (r[j] - e) ** 2 / e
    return s


def category_test(records, n_perm=10000, seed=0):
    """Permutation test of 'fix rate is independent of category'."""
    cats = [r["category"] for r in records]
    ys = [1 if r["fixed"] else 0 for r in records]
    def table(c, y):
        t = {k: [0, 0] for k in CATS}
        for ci, yi in zip(c, y):
            t[ci][0 if yi else 1] += 1
        return [t[k] for k in CATS]
    obs = chi2_stat(table(cats, ys))
    if obs == 0:
        return obs, 1.0, None
    rng = random.Random(seed)
    ge = 0
    yp = list(ys)
    for _ in range(n_perm):
        rng.shuffle(yp)
        if chi2_stat(table(cats, yp)) >= obs - 1e-12:
            ge += 1
    p_perm = (ge + 1) / (n_perm + 1)
    try:
        from scipy.stats import chi2
        p_asym = float(chi2.sf(obs, df=len([k for k in CATS if any(c == k for c in cats)]) - 1))
    except Exception:
        p_asym = None
    return obs, p_perm, p_asym


def main(run_dir):
    recs = [json.loads(l) for l in open(os.path.join(run_dir, "results.jsonl"))]
    conds = [c for c in ["zero_shot", "iterative", "sampled"] if any(r["condition"] == c for r in recs)]
    by = defaultdict(list)
    for r in recs:
        by[(r["condition"], r["category"])].append(r)
        by[(r["condition"], "ALL")].append(r)

    md = [f"# Results for run `{os.path.basename(os.path.normpath(run_dir))}`",
          f"Model: `{recs[0]['model']}`  |  records: {len(recs)}\n",
          "## Fix rate by category and condition (Wilson 95% CI)\n",
          "| Condition | Category | Fixed / n | Rate | 95% CI |", "|---|---|---|---|---|"]
    rows = []
    for c in conds:
        for cat in CATS + ["ALL"]:
            g = by[(c, cat)]
            if not g:
                continue
            k, n = sum(r["fixed"] for r in g), len(g)
            lo, hi = wilson(k, n)
            rows.append({"condition": c, "category": cat, "fixed": k, "n": n,
                         "rate": round(k / n, 3), "ci_low": round(lo, 3), "ci_high": round(hi, 3)})
            md.append(f"| {c} | {cat} | {k}/{n} | {k/n:.2f} | [{lo:.2f}, {hi:.2f}] |")
    with open(os.path.join(run_dir, "fix_rates.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    md.append("\n## H1: category effect (per condition)\n")
    md.append("| Condition | Chi-square | p (permutation) | p (asymptotic, indicative) |")
    md.append("|---|---|---|---|")
    for c in conds:
        stat, pp, pa = category_test([r for r in recs if r["condition"] == c])
        md.append(f"| {c} | {stat:.2f} | {pp:.3f} | {'n/a' if pa is None else f'{pa:.3f}'} |")

    md.append("\n## H2 and control: paired comparisons (exact McNemar)\n")
    md.append("| Comparison | Only A fixed | Only B fixed | Both | Neither | p |")
    md.append("|---|---|---|---|---|---|")
    idx = {(r["condition"], r["bug_id"]): r["fixed"] for r in recs}
    bug_ids = sorted({r["bug_id"] for r in recs})
    for a, b in [("zero_shot", "iterative"), ("sampled", "iterative"), ("zero_shot", "sampled")]:
        if a not in conds or b not in conds:
            continue
        pairs = [(idx[(a, i)], idx[(b, i)]) for i in bug_ids if (a, i) in idx and (b, i) in idx]
        only_a = sum(x and not y for x, y in pairs); only_b = sum(y and not x for x, y in pairs)
        both = sum(x and y for x, y in pairs); neither = sum(not x and not y for x, y in pairs)
        md.append(f"| A={a} vs B={b} | {only_a} | {only_b} | {both} | {neither} | "
                  f"{mcnemar_exact(only_a, only_b):.3f} |")

    if "zero_shot" in conds and "iterative" in conds:
        md.append("\n## Sub-question: gain from iterative prompting per category\n")
        md.append("| Category | Zero-shot | Iterative | Difference (pp) |")
        md.append("|---|---|---|---|")
        for cat in CATS:
            z, it = by[("zero_shot", cat)], by[("iterative", cat)]
            if z and it:
                rz, ri = sum(r["fixed"] for r in z) / len(z), sum(r["fixed"] for r in it) / len(it)
                md.append(f"| {cat} | {rz:.2f} | {ri:.2f} | {100*(ri-rz):+.0f} |")

    md.append("\n## Final failure types\n")
    ft = Counter((r["condition"], r["failure_type"]) for r in recs)
    types = sorted({t for _, t in ft})
    md.append("| Condition | " + " | ".join(types) + " |")
    md.append("|---|" + "---|" * len(types))
    frows = []
    for c in conds:
        md.append(f"| {c} | " + " | ".join(str(ft[(c, t)]) for t in types) + " |")
        frows.append({"condition": c, **{t: ft[(c, t)] for t in types}})
    with open(os.path.join(run_dir, "failure_types.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["condition"] + types)
        w.writeheader(); w.writerows(frows)

    if any(r["condition"] == "iterative" for r in recs):
        tu = Counter(r["turns_used"] for r in recs if r["condition"] == "iterative" and r["fixed"])
        md.append("\nIterative condition - turns needed for successful fixes: "
                  + ", ".join(f"{k} turn(s): {v}" for k, v in sorted(tu.items())))

    with open(os.path.join(run_dir, "summary.md"), "w") as f:
        f.write("\n".join(md) + "\n")
    print("\n".join(md))

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7, 3.6))
        width = 0.8 / len(conds)
        colors = ["#4C72B0", "#DD8452", "#55A868"]
        for i, c in enumerate(conds):
            vals, errs_lo, errs_hi = [], [], []
            for cat in CATS:
                rr = [x for x in rows if x["condition"] == c and x["category"] == cat]
                if rr:
                    vals.append(rr[0]["rate"]); errs_lo.append(rr[0]["rate"] - rr[0]["ci_low"])
                    errs_hi.append(rr[0]["ci_high"] - rr[0]["rate"])
                else:
                    vals.append(0); errs_lo.append(0); errs_hi.append(0)
            xs = [j + i * width for j in range(len(CATS))]
            ax.bar(xs, vals, width, yerr=[errs_lo, errs_hi], capsize=3, label=c, color=colors[i])
        ax.set_xticks([j + width * (len(conds) - 1) / 2 for j in range(len(CATS))])
        ax.set_xticklabels(CATS)
        ax.set_ylim(0, 1.05); ax.set_ylabel("Fix rate")
        ax.set_title(f"Fix rate by bug category ({recs[0]['model']})", fontsize=10)
        ax.legend(frameon=False, fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        fig.tight_layout()
        fig.savefig(os.path.join(run_dir, "fix_rates.png"), dpi=160)
    except ImportError:
        pass


if __name__ == "__main__":
    main(sys.argv[1])
