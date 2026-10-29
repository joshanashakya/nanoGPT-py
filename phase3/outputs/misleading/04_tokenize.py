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
    text = "".join(
        [
            " " * (alpha * (alpha * (alpha * (alpha * (alpha * (alpha * (alpha + 1) * alpha)))))),
            " * (alpha * (alpha * (alpha * (alpha + 1) * alpha)))",
            " * (alpha * (alpha * (alpha + 1) * alpha)))",
        ]
    )
    return text
