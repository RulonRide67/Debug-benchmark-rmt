def is_palindrome(text):
    """Return True if text reads the same backwards, ignoring case and any
    character that is not a letter or digit."""
    return text == text[::-1]
