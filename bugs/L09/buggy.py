def is_prime(n):
    """Return True if the integer n is a prime number."""
    for d in range(2, n):
        if n % d == 0:
            return False
    return True
