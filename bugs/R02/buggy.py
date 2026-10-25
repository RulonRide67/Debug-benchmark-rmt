def word_counts(text):
    """Return a dict mapping each lower-cased word in text to how often it occurs."""
    counts = {}
    for word in text.lower().split():
        counts[word] += 1
    return counts
