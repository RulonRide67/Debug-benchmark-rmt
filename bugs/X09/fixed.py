import hmac

def check_api_key(provided, expected):
    """Return True if the provided API key equals the expected one. The comparison
    must take constant time (use a constant-time compare function)."""
    return hmac.compare_digest(provided.encode(), expected.encode())
