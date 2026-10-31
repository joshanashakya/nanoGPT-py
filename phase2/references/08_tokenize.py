def tokenize(self, s):
    lines = s.splitlines()
    # If requested, strip off blank lines.
    if self._blanklines == "discard":
        lines = [l for l in lines if l.rstrip()]
    elif self._blanklines == "discard-eof":
        if lines and not lines[-1].strip():
            lines.pop()
    return lines