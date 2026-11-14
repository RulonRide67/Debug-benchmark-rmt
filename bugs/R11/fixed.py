def to_dict(pairs):
    """Convert strings such as 'key=value' into a dict. Only the first '=' separates
    key and value; entries without '=' are ignored."""
    result = {}
    for p in pairs:
        if "=" in p:
            key, value = p.split("=", 1)
            result[key] = value
    return result
