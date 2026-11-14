def format_log(user, action):
    """Return a single log line 'user=<user> action=<action>'. Any newline or
    carriage-return character in the inputs must be replaced by '_'."""
    def clean(s):
        return s.replace("\r", "_").replace("\n", "_")
    return f"user={clean(user)} action={clean(action)}"
