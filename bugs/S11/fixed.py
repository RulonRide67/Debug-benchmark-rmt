def count_down(n):
    """Return the list [n, n-1, ..., 1]; an empty list if n < 1."""
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result
