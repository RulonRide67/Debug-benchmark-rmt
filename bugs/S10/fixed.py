def total_length(words):
    """Return the total number of characters in all words."""
    total = 0
    for word in words:
        total += len(word)
    return total
