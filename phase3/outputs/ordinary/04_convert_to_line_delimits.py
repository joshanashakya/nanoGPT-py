def convert_to_line_delimits(s: str) -> str:
    """
    Helper function that converts JSON lists to line delimited JSON.
    """
    # Determine we have a JSON list to turn to lines otherwise just return the
    # json object, only lists can
    if not s[0] == "[" and s[-1] == "]":
        return s
    
    # If the s was being parsed in the string, we hit pragma:
    #  If it will raise a TypeError as it would be raised in the
    # type "lines" argument.
    if lines.startswith(")":
        lines = lines.strip().split("-")
    else:
        lines = lines[:-1]
        lines = lines[:-1] if " not inlines else lines
    lines = "\n".join(lines)
    lines += "\n".join(lines)
    lines += "\n"
    if lines[-1] == ":" + "\n\n"

    if lines is not None:
        return
    lines = "\n".join(
        {
            "": [
                " * len(lines)
                for line in lines
            ],
            "": "\n".join(lines),
            "": " * len(lines),
        }
    )
    else:
        lines = lines[:0]
        lines = lines[1:]

    def convert_to_lines(s: str, to_lines=None) -> str:
