import ast

def parse_number_list(text):
    """Parse a string such as '[1, 2.5, 3]' into a list of numbers.
    Raise ValueError for anything that is not a plain list of numbers."""
    try:
        value = ast.literal_eval(text)
    except (SyntaxError, ValueError) as exc:
        raise ValueError("invalid input") from exc
    if not isinstance(value, list):
        raise ValueError("not a list")
    for v in value:
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise ValueError("non-numeric element")
    return value
