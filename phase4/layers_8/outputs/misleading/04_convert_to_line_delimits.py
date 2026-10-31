def convert_to_line_delimits(s: str) -> str:
    """
    Helper function that converts lists of tuples to line delimited JSON.
    """
    # Determine we have a JSON list to turn to lines otherwise just return the
    # json object, only lists can
    if not s[0] == "[" and s[-1] == "]":
        return s
    s = s[1:-1]
    if not s.startswith(">"):
        return s
    if not s.startswith(">"):
        return s[:len(">")] + "]"
    if not s.startswith(">"):
        return s[:len(">")] + "]"
    try:
        return s[len(">")] + "]" + ":[")
    except TypeError:
        if s[-1] == ">":
            return s[-1] + "."

    return s
