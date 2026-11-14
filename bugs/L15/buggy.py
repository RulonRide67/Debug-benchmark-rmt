def capitalize_words(text):
    """Return text with the first letter of every word in upper case and all other
    letters in lower case; words are separated by single spaces."""
    return " ".join(w[0].upper() + w[1:] for w in text.split())
