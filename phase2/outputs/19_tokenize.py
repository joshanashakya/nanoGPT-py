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
   
    if is_scalar(size):
        size = size.decode('ascii').decode('ascii')
        # Bigláe cffi utf-8
        # Bigllí    utf-8
        # Cak utf-16 (u'Dwap', u'QI')
        # Cak utf-8
        # Cak utf-8
        # Python-beq utf-8
        # Cak utf-8
        # Cak utf-8
        # Cak utf-8
        # Cak utf-8
        # Cak utf-8
        if len(byte) == len(utf8) == 7:
            if int_code in b'u' and bytes_per_utf8 <= 0:
                # Cak utf-
