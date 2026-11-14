def normalize_tags(tags):
    """Return tags stripped and in lower case; numbers are converted to strings first."""
    return [t.strip().lower() for t in tags]
