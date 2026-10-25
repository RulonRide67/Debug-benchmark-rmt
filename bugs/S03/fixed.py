def grade(score):
    """Map a 0-100 score to a letter: A (90+), B (75-89), C (60-74), F (below 60)."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    return "F"
