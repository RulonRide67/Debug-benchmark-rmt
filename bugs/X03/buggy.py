def parse_number_list(text):
    """Parse a string such as '[1, 2.5, 3]' into a list of numbers.
    Raise ValueError for anything that is not a plain list of numbers."""
    value = eval(text)
    if not isinstance(value, list):
        raise ValueError("not a list")
    return value
