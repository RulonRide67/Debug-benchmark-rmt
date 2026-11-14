def chunk(items, size):
    """Split the list items into consecutive chunks of length size; the last chunk
    may be shorter."""
    count = len(items) / size
    return [items[i * size:(i + 1) * size] for i in range(count)]
