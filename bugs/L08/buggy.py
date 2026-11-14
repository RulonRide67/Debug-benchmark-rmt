def median(values):
    """Return the median of a non-empty list of numbers."""
    s = sorted(values)
    return s[len(s) // 2]
