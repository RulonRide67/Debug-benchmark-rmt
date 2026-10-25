import sqlite3

def find_user(conn, username):
    """Return (id, username) of the user whose username is exactly `username`, or None."""
    cur = conn.execute("SELECT id, username FROM users WHERE username = ?", (username,))
    return cur.fetchone()
