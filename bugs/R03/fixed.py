def differences(values):
    """Return the list of differences between neighbours: values[i+1] - values[i]."""
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]
