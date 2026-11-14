def clamp(x, low, high):
    """Return x limited to the closed interval [low, high]."""
    return max(low, min(x, high))
