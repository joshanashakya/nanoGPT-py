def tokenize(self, s):
    lines = s.splitlines()
    # If requested, strip off blank lines.
    if self._blanklines == "discard":
        lines = [l for l in lines if l.rstrip()]
  