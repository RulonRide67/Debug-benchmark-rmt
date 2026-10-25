def apply_discount(price, percent):
    """Return price after a percentage discount, never below zero, rounded to 2 decimals."""
    discounted = price * (1 - percent / 100)
    return round(max(discounted, 0), 2)
