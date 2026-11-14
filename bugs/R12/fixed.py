def max_score(scores):
    """Return the highest score, ignoring None entries; None if there are no numbers."""
    numbers = [s for s in scores if s is not None]
    if not numbers:
        return None
    return max(numbers)
