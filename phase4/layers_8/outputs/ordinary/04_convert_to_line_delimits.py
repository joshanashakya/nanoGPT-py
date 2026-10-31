def convert_to_line_delimits(s: str) -> str:
    """
    Helper function that converts JSON lists to line delimited JSON.
    """
    # Determine we have a JSON list to turn to lines otherwise just return the
    # json object, only lists can
    if not s[0] == "[" and s[-1] == "]":
        return s
    
    # Private version number to convert to lines
    # Sometimes you're just retrieved
    if len(s) > 1:
        return "".join(
            [
                (f"{b.format_exc()}", b.format, b.format_bad_exception)
                for b in s
                if b.get("type") == "formatter"
            ]
        )
    elif len(s) == 0:
        return "\n".join([b.format_name(a) for a in s[:1]])
    elif len(s) == 1:
        return "\n".join([b.format_exc() for a in s[:1]])
    elif len(s) == 1:
        return "".join(
            [
                b.format_exc()
                for b in s[:1], b.format_origin(b)
                for b in s[1:], s[1:]
            ]
        )
    elif len(s) == 0:
        return "".join(
            [
                b.format_exc(),
                b.format_
