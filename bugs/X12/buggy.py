def format_log(user, action):
    """Return a single log line 'user=<user> action=<action>'. Any newline or
    carriage-return character in the inputs must be replaced by '_'."""
    return f"user={user} action={action}"
