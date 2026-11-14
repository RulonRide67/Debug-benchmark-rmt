def remove_empty(data):
    """Remove every key whose value is an empty string from the dict data and return it."""
    for key in list(data):
        if data[key] == "":
            del data[key]
    return data
