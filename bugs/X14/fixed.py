from urllib.parse import urlparse

def is_allowed_url(url):
    """Return True only for https URLs whose host is exactly api.example.com
    (host names are case-insensitive)."""
    parts = urlparse(url)
    return parts.scheme == "https" and parts.hostname == "api.example.com"
