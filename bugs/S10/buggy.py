def total_length(words):
    """Return the total number of characters in all words."""
    total = 0
    for class in words:
        total += len(class)
    return total
