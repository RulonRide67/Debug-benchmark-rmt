def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text, ignoring case."""
    total = 0
    for ch in text.lower():
        if ch in "aeiou":
            total += 1
    return total
