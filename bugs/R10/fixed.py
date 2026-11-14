def initials(full_name):
    """Return initials such as 'A.L.' for 'Ada Lovelace'; extra spaces are ignored."""
    parts = full_name.split()
    return "".join(p[0].upper() + "." for p in parts)
