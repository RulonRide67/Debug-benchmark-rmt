def average(values):
    """Return the arithmetic mean of values, or None for an empty sequence."""
    if len(values) == 0:
        return None
    return sum(values) / len(values)
