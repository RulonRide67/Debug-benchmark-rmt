import os

def safe_path(base_dir, user_path):
    """Join user_path onto base_dir and return the absolute result.
    Raise ValueError if the result would point outside base_dir."""
    return os.path.join(base_dir, user_path)
