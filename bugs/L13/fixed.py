def unique_in_order(items):
    """Return items without duplicates, keeping the first occurrence of each
    value in its original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
