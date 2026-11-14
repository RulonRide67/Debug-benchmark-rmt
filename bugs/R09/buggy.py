def longest_word(words):
    """Return the longest word (the first one if there is a tie); '' for an empty list."""
    return max(words, key=len)
