import hashlib

def hash_password(password, salt):
    """Return the hex digest of PBKDF2-HMAC-SHA256 over password with the given salt
    (both str, UTF-8) and 100000 iterations."""
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000).hex()
