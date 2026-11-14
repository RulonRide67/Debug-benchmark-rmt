import json

def user_to_json(user):
    """Return the user dict as a JSON string without the 'password' and 'token'
    fields. The input dict must not be modified."""
    safe = {k: v for k, v in user.items() if k not in ("password", "token")}
    return json.dumps(safe)
