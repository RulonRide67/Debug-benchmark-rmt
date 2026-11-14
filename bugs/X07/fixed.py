import json

def load_settings(data):
    """data is bytes containing settings as a JSON object. Return them as a dict.
    Untrusted data must never execute code; raise ValueError for anything that is
    not a JSON object."""
    value = json.loads(data)
    if not isinstance(value, dict):
        raise ValueError("settings must be a JSON object")
    return value
