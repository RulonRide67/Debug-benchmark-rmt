ALLOWED = {"name", "email", "bio"}

def update_profile(profile, changes):
    """Apply changes to the profile dict and return it. Only the keys 'name',
    'email' and 'bio' may be changed; all other keys in changes are ignored."""
    for key, value in changes.items():
        if key in ALLOWED:
            profile[key] = value
    return profile
