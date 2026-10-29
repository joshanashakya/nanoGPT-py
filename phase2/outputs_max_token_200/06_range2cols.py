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
    col_var = "C"
    if not as_integer(is_integer(idx_var)):
        raise ValueError("Not all indices of idx_var")

    if np.any(is_numeric(idx_var)):
        raise ValueError("Not all indices of idx_var")

    # Fixth (above) the data-based-column indices
    idx_idx = list("ABCD")

    # Iterable indices to keep track of indices
    idx_idx = list(idx_idx)

    result_indices = defaultdict(list)
    result_indices = defaultdict(lambda: defaultdict(lambda: np.number))

    if not as_integer(result_indices):
        # Split to int/float column, so a single-element list
        result_indices = defaultdict(lambda: np.number)

    result_indices =
