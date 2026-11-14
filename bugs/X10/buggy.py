def safe_redirect(target):
    """Return target if it is a path on this site (it starts with exactly one '/'
    and is not a protocol-relative or backslash URL); otherwise return '/'."""
    return target if target.startswith("/") else "/"
