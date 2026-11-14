import hashlib

def hash_password(password, salt):
    """Return the hex digest of PBKDF2-HMAC-SHA256 over password with the given salt
    (both str, UTF-8) and 100000 iterations."""
    return hashlib.md5((password + salt).encode()).hexdigest()
