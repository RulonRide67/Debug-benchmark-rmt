# Results for run `pilot_qwen7b`
Model: `ollama:qwen2.5-coder:7b`  |  records: 48

## Fix rate by category and condition (Wilson 95% CI)

| Condition | Category | Fixed / n | Rate | 95% CI |
|---|---|---|---|---|
| zero_shot | syntax | 3/4 | 0.75 | [0.30, 0.95] |
| zero_shot | logic | 3/4 | 0.75 | [0.30, 0.95] |
| zero_shot | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| zero_shot | security | 2/4 | 0.50 | [0.15, 0.85] |
| zero_shot | ALL | 12/16 | 0.75 | [0.51, 0.90] |
| iterative | syntax | 3/4 | 0.75 | [0.30, 0.95] |
| iterative | logic | 3/4 | 0.75 | [0.30, 0.95] |
| iterative | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | security | 2/4 | 0.50 | [0.15, 0.85] |
| iterative | ALL | 12/16 | 0.75 | [0.51, 0.90] |
| sampled | syntax | 4/4 | 1.00 | [0.51, 1.00] |
| sampled | logic | 3/4 | 0.75 | [0.30, 0.95] |
| sampled | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| sampled | security | 3/4 | 0.75 | [0.30, 0.95] |
| sampled | ALL | 14/16 | 0.88 | [0.64, 0.97] |

## H1: category effect (per condition)

| Condition | Chi-square | p (permutation) | p (asymptotic, indicative) |
|---|---|---|---|
| zero_shot | 2.67 | 0.856 | 0.446 |
| iterative | 2.67 | 0.856 | 0.446 |
| sampled | 2.29 | 1.000 | 0.515 |

## H2 and control: paired comparisons (exact McNemar)

| Comparison | Only A fixed | Only B fixed | Both | Neither | p |
|---|---|---|---|---|---|
| A=zero_shot vs B=iterative | 0 | 0 | 12 | 4 | 1.000 |
| A=sampled vs B=iterative | 2 | 0 | 12 | 2 | 0.500 |
| A=zero_shot vs B=sampled | 0 | 2 | 12 | 2 | 0.500 |

## Sub-question: gain from iterative prompting per category

| Category | Zero-shot | Iterative | Difference (pp) |
|---|---|---|---|
| syntax | 0.75 | 0.75 | +0 |
| logic | 0.75 | 0.75 | +0 |
| runtime | 1.00 | 1.00 | +0 |
| security | 0.50 | 0.50 | +0 |

## Final failure types

| Condition | fixed | overfit_visible | tests_fail |
|---|---|---|---|
| zero_shot | 12 | 3 | 1 |
| iterative | 12 | 4 | 0 |
| sampled | 14 | 2 | 0 |

Iterative condition - turns needed for successful fixes: 1 turn(s): 12
