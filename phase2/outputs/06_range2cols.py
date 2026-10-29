def _range2cols(areas: str) -> list[int]:
    """
    Convert comma separated list of column names and ranges to indices.

    Parameters
    ----------
    areas : str
        A string containing a sequence of column ranges (or areas).

    Returns
    -------
    cols : list
        A list of 0-based column indices.

    Examples
    --------
    >>> _range2cols("A:E")
    [0, 1, 2, 3, 4]
    >>> _range2cols("A,C,Z:AB")
    [0, 2, 25, 26, 27]
    """
    _slice1 = 0
    _slice2 = 0

    def _slice2d(label):
        """
        Convert the given label that match order and column k.

        Parameters
        ----------
        label : np.timedelta64

        Returns
        -------
        labels : str
           A string containing a single column label.

        Notes
        -----
        The index is converted to :doc:`"a"`. A common DATA, `label`
        is externally not the valid placebook of
        ``label()`` method, which returns the original object for
        ``label()`` method.

        """
        label = np.timedelta64(label, len(labels))
        return [label]

    def _validate_indexer(self, column, kind):
        """
        Boolean missing in self._validate_indexer(self.label, kind)

        Parameters
        ----------
        column : np.ndarray[np.intp] or ndarray[np.intp]
            If a Series, it is converted to an Index.
        kind : str, default "index"
            Whether the column is a MultiIndex or
