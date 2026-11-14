def chunk(items, size):
    """Split the list items into consecutive chunks of length size; the last chunk
    may be shorter."""
    return [items[i:i + size] for i in range(0, len(items), size)]
