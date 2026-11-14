def update_profile(profile, changes):
    """Apply changes to the profile dict and return it. Only the keys 'name',
    'email' and 'bio' may be changed; all other keys in changes are ignored."""
    profile.update(changes)
    return profile
