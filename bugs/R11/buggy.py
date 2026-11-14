def to_dict(pairs):
    """Convert strings such as 'key=value' into a dict. Only the first '=' separates
    key and value; entries without '=' are ignored."""
    return dict(p.split("=") for p in pairs)
