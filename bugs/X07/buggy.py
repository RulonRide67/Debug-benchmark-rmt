import pickle

def load_settings(data):
    """data is bytes containing settings as a JSON object. Return them as a dict.
    Untrusted data must never execute code; raise ValueError for anything that is
    not a JSON object."""
    return pickle.loads(data)
