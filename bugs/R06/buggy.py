def get_city(user):
    """user is a dict that may contain an 'address' dict with a 'city' key.
    Return the city, or 'unknown' if it is not available."""
    return user.get("address").get("city", "unknown")
