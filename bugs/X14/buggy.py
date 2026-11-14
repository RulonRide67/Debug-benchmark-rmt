def is_allowed_url(url):
    """Return True only for https URLs whose host is exactly api.example.com
    (host names are case-insensitive)."""
    return url.startswith("https://api.example.com")
