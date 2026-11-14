def compound_balance(principal, rate_percent, years):
    """Return the balance after compounding annually at rate_percent per year,
    rounded to 2 decimals."""
    return round(principal * (1 + rate_percent) ** years, 2)
