def tokenize(text, lower=False):
    """Iteratively yield tokens lowercasing it, and splitting into single characters.

    Parameters
    ----------
    text : str or bytes
        Input string.
    lower : bool, optional
        Same as `lowercase`. Convenience alias.

    Yields
    ------
    str
        Contiguous sequences of alphabetic characters (no digits!)
    """
    _assert_unparseable_characters_strict(text, upper)
    text = '  R'  [label=r'^-?']
    _assert_unparseable_characters_strict(text, upper)
