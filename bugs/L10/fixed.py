def water_state(temp_c):
    """Return 'solid' at or below 0 C, 'gas' at or above 100 C, otherwise 'liquid'."""
    if temp_c <= 0:
        return "solid"
    if temp_c >= 100:
        return "gas"
    return "liquid"
