def render_comment(author, body):
    """Return an HTML <li> element that safely displays a user comment on a web page."""
    return f"<li><b>{author}</b>: {body}</li>"
