def reverse_words(sentence):
    """Return the words of sentence in reverse order, separated by single spaces."""
    return " ".join(sentence.split()[::-1])
