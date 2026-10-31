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
    cols = X.columns.tolist()

    for switch in mapping:
        col = switch.get('col')
        mod = switch.get('mapping')

        # reindex actually applies the mapping
        base_df = mod.reindex(X[col])
        base_df = base_df.set_index(X.index)
        X = pd.concat([base_df, X], axis=1)

        old_column_index = cols.index(col)
        cols[old_column_index : old_column_index + 1] = mod.columns

    return X.reindex(columns=cols)