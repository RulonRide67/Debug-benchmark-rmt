import secrets

def generate_token():
    """Return a 32-character hexadecimal session token from a cryptographically
    secure random source."""
    return secrets.token_hex(16)
