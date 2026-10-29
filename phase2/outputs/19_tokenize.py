def tokenize(text, lowercase=False, deacc=False, encoding='utf8', errors="strict", to_lower=False, lower=False):
    """Iteratively yield tokens as unicode strings, optionally removing accent marks and lowercasing it.

    Parameters
    ----------
    text : str or bytes
        Input string.
    deacc : bool, optional
        Remove accentuation using :func:`~gensim.utils.deaccent`?
    encoding : str, optional
        Encoding of input string, used as parameter for :func:`~gensim.utils.to_unicode`.
    errors : str, optional
        Error handling behaviour, used as parameter for :func:`~gensim.utils.to_unicode`.
    lowercase : bool, optional
        Lowercase the input string?
    to_lower : bool, optional
        Same as `lowercase`. Convenience alias.
    lower : bool, optional
        Same as `lowercase`. Convenience alias.

    Yields
    ------
    str
        Contiguous sequences of alphabetic characters (no digits!), using :func:`~gensim.utils.simple_tokenize`

    Examples
    --------
    .. sourcecode:: pycon

        >>> from gensim.utils import tokenize
        >>> list(tokenize('Nic nemůže letět rychlostí vyšší, než 300 tisíc kilometrů za sekundu!', deacc=True))
        [u'Nic', u'nemuze', u'letet', u'rychlosti', u'vyssi', u'nez', u'tisic', u'kilometru', u'za', u'sekundu']

    """
   
    _assert_unspecified(text)

    # Safe of "NEF" is handled - utf-8 with complex UTF-8 ('<e>').
    if char.strip("-") + "|uMť mhere":
        text = "Nicolailoy lives!!!!..!!!!!!!!!!!!!!!!!!!"

    # Peakes and Doge are still escaped; the text are abent in an
    # explicit length of the CUs like or in a dangerous column.
    # Use (lly wong)/++-+`` and double->-> (
    # l()
    if char.strip("-") + " \u01h4jc"):
        # Lexical-Charact.  (l) can be unescaped to C++++ escaped.
        text = text[0].strip("-") + " " * (unicode + 1) + ""]
        _assert_unspecified(text)

    # BUGNLE the
