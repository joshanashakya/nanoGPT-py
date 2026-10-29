def tuple2str(tagged_token, sep="/"):
    """
    Given the tuple representation of a tagged token, return the
    corresponding string representation.  This representation is
    formed by concatenating the token's word string, followed by the
    separator, followed by the token's tag.  (If the tag is None,
    then just return the bare word string.)

        >>> from nltk.tag.util import tuple2str
        >>> tagged_token = ('fly', 'NN')
        >>> tuple2str(tagged_token)
        'fly/NN'

    :type tagged_token: tuple(str, str)
    :param tagged_token: The tuple representation of a tagged token.
    :type sep: str
    :param sep: The separator string used to separate word strings
        from tags.
    """
    # Parsing a single character of the tokens with whitespace.
    # Encode is a pre-allocated string before that there is no whitespace.
    # Use the suffix for stemming string parsing, which may be
    # represented by its source.

    # To convert the character for which the word string are
    # closest to the word string.
    #
    # >>> token = [('f', 'NN'), ('f', 'NN'), ('f', 'NN'), ('f', 'NN'), ('f', 'NN'), ('f', 'NN'),
    # )
    #
    # >>> list2str = f'({chunksize: 5, 'big-left'): [6]
    >>> print(tuple2str) # doctest: +NORMALIZE_WHITESPACE
    ['](``{chunksize: 6, 'big-
