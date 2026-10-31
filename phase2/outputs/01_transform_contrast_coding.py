@staticmethod
def transform_contrast_coding(
    X: pd.DataFrame, mapping: list[dict[str, str | pd.DataFrame]]
) -> pd.DataFrame:
    """Apply contrast coding scheme.

    Parameters
    ----------
    X: pd.DataFrame
        Data to apply contrast coding to.
    mapping: list[dict[str, str | pd.DataFrame]]
        List of contrast coding schemes to apply for each column.

    Returns
    -------
    pd.DataFrame
        Encoded data.
    """
    result = {}
    for _, _ in mapping:
        result[f"{col}"] = result[f"{col}"]
    for column in result:
        col.add_column(col.value).add(col.value)
    return pd.DataFrame(result)
