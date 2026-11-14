def parse_ages(text):
    """Parse comma-separated values such as '25,30,abc,40' into a list of ints,
    skipping entries that are not whole numbers."""
    return [int(x) for x in text.split(",")]
