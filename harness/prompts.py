"""Fixed prompt templates. The same wording is used for every bug; the bug category is
never revealed to the model."""
import re

SYSTEM = ("You are a careful Python developer. You fix bugs in code. "
          "Always answer with the complete corrected code in one ```python code block.")

ZERO_SHOT = """The following Python code contains a bug. The docstring describes the intended behaviour.
Find the bug and return the complete corrected code. Keep the same function name and signature.

```python
{code}
```"""

FEEDBACK = """Your corrected code still does not work. Running the tests produced this output:

```
{test_output}
```

Fix the problem and return the complete corrected code again."""


def extract_code(response):
    """Takes the last ```python block; falls back to any fenced block; else None."""
    blocks = re.findall(r"```(?:python|py)?[ \t]*\n(.*?)```", response, re.S)
    if blocks:
        return blocks[-1]
    return None
