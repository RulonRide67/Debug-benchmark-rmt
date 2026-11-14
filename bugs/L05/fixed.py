def is_palindrome(text):
    """Return True if text reads the same backwards, ignoring case and any
    character that is not a letter or digit."""
    clean = [ch.lower() for ch in text if ch.isalnum()]
    return clean == clean[::-1]
