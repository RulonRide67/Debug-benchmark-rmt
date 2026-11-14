def repeat_text(text, times):
    """Return text repeated `times` times. Raise ValueError if times is negative or
    the result would be longer than 10000 characters."""
    if times < 0 or len(text) * times > 10000:
        raise ValueError("invalid repeat count")
    return text * times
