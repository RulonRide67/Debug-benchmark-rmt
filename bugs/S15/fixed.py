def max_of_three(a, b, c):
    """Return the largest of the three numbers."""
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result
