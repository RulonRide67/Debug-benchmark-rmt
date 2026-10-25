# Results for run `pipeline_check_mock_feedback`
Model: `mock:fix_after_feedback`  |  records: 48

## Fix rate by category and condition (Wilson 95% CI)

| Condition | Category | Fixed / n | Rate | 95% CI |
|---|---|---|---|---|
| zero_shot | syntax | 0/4 | 0.00 | [0.00, 0.49] |
| zero_shot | logic | 0/4 | 0.00 | [0.00, 0.49] |
| zero_shot | runtime | 0/4 | 0.00 | [0.00, 0.49] |
| zero_shot | security | 0/4 | 0.00 | [0.00, 0.49] |
| zero_shot | ALL | 0/16 | 0.00 | [0.00, 0.19] |
| iterative | syntax | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | logic | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | runtime | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | security | 4/4 | 1.00 | [0.51, 1.00] |
| iterative | ALL | 16/16 | 1.00 | [0.81, 1.00] |
| sampled | syntax | 0/4 | 0.00 | [0.00, 0.49] |
| sampled | logic | 0/4 | 0.00 | [0.00, 0.49] |
| sampled | runtime | 0/4 | 0.00 | [0.00, 0.49] |
| sampled | security | 0/4 | 0.00 | [0.00, 0.49] |
| sampled | ALL | 0/16 | 0.00 | [0.00, 0.19] |

## H1: category effect (per condition)

| Condition | Chi-square | p (permutation) | p (asymptotic, indicative) |
|---|---|---|---|
| zero_shot | 0.00 | 1.000 | n/a |
| iterative | 0.00 | 1.000 | n/a |
| sampled | 0.00 | 1.000 | n/a |

## H2 and control: paired comparisons (exact McNemar)

| Comparison | Only A fixed | Only B fixed | Both | Neither | p |
|---|---|---|---|---|---|
| A=zero_shot vs B=iterative | 0 | 16 | 0 | 0 | 0.000 |
| A=sampled vs B=iterative | 0 | 16 | 0 | 0 | 0.000 |
| A=zero_shot vs B=sampled | 0 | 0 | 0 | 16 | 1.000 |

## Sub-question: gain from iterative prompting per category

| Category | Zero-shot | Iterative | Difference (pp) |
|---|---|---|---|
| syntax | 0.00 | 1.00 | +100 |
| logic | 0.00 | 1.00 | +100 |
| runtime | 0.00 | 1.00 | +100 |
| security | 0.00 | 1.00 | +100 |

## Final failure types

| Condition | fixed | syntax_error | tests_fail |
|---|---|---|---|
| zero_shot | 0 | 4 | 12 |
| iterative | 16 | 0 | 0 |
| sampled | 0 | 4 | 12 |

Iterative condition - turns needed for successful fixes: 2 turn(s): 16
