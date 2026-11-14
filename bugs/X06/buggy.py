import random

def generate_token():
    """Return a 32-character hexadecimal session token from a cryptographically
    secure random source."""
    return "%032x" % random.getrandbits(128)
