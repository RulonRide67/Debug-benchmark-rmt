def cart_total(cart, prices):
    """cart maps item -> quantity, prices maps item -> unit price. Return the total
    cost; items without a known price are skipped."""
    return sum(qty * prices[item] for item, qty in cart.items())
