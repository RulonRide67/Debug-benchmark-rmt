import re

def build_ping_command(host):
    """Return the argument list for running 'ping -c 1 <host>' without a shell.
    Raise ValueError unless host consists only of letters, digits, dots and hyphens
    and does not start with a hyphen."""
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*", host):
        raise ValueError("invalid host")
    return ["ping", "-c", "1", host]
