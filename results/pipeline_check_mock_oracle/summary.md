# Results for run `pipeline_check_mock_oracle`
Model: `mock:oracle`  |  records: 48

## Fix rate by category and condition (Wilson 95% CI)

| Condition | Category | Fixed / n | Rate | 95% CI |
|---|---|---|---|---|
| zero_shot | syntax | 4/4 | 1.00 | [0.51, 1.00] |
| zero_shot | logic | 4/4 | 1.00 | [0.51, 1.00] |
| zero_shot | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| zero_shot | security | 4/4 | 1.00 | [0.51, 1.00] |
| zero_shot | ALL | 16/16 | 1.00 | [0.81, 1.00] |
| iterative | syntax | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | logic | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | security | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | ALL | 16/16 | 1.00 | [0.81, 1.00] |
| sampled | syntax | 4/4 | 1.00 | [0.51, 1.00] |
| sampled | logic | 4/4 | 1.00 | [0.51, 1.00] |
| sampled | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| sampled | security | 4/4 | 1.00 | [0.51, 1.00] |
| sampled | ALL | 16/16 | 1.00 | [0.81, 1.00] |

## H1: category effect (per condition)

| Condition | Chi-square | p (permutation) | p (asymptotic, indicative) |
|---|---|---|---|
| zero_shot | 0.00 | 1.000 | n/a |
| iterative | 0.00 | 1.000 | n/a |
| sampled | 0.00 | 1.000 | n/a |

## H2 and control: paired comparisons (exact McNemar)

| Comparison | Only A fixed | Only B fixed | Both | Neither | p |
|---|---|---|---|---|---|
| A=zero_shot vs B=iterative | 0 | 0 | 16 | 0 | 1.000 |
| A=sampled vs B=iterative | 0 | 0 | 16 | 0 | 1.000 |
| A=zero_shot vs B=sampled | 0 | 0 | 16 | 0 | 1.000 |

## Sub-question: gain from iterative prompting per category

| Category | Zero-shot | Iterative | Difference (pp) |
|---|---|---|---|
| syntax | 1.00 | 1.00 | +0 |
| logic | 1.00 | 1.00 | +0 |
| runtime | 1.00 | 1.00 | +0 |
| security | 1.00 | 1.00 | +0 |

## Final failure types

| Condition | fixed |
|---|---|
| zero_shot | 16 |
| iterative | 16 |
| sampled | 16 |

Iterative condition - turns needed for successful fixes: 1 turn(s): 16
