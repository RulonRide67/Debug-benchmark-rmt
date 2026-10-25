def merge_dicts(a, b):
    """Return a new dict with the keys of a and b; values from b win on conflict."""
    result = dict(a)
    for key, value in b.items():
        result[key] = value
    return result
