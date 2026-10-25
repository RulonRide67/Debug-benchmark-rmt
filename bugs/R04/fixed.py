def format_receipt(items):
    """items is a list of (name, qty, unit_price). Return one line per item in the
    form 'name x<qty> = <cost>' and a last line 'TOTAL = <total>', money with 2 decimals."""
    lines = []
    total = 0
    for name, qty, price in items:
        cost = qty * price
        total += cost
        lines.append(name + " x" + str(qty) + " = " + f"{cost:.2f}")
    lines.append("TOTAL = " + f"{total:.2f}")
    return "\n".join(lines)
