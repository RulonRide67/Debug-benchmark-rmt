import os

def safe_path(base_dir, user_path):
    """Join user_path onto base_dir and return the absolute result.
    Raise ValueError if the result would point outside base_dir."""
    base = os.path.realpath(base_dir)
    full = os.path.realpath(os.path.join(base, user_path))
    if os.path.commonpath([base, full]) != base:
        raise ValueError("path escapes base directory")
    return full
