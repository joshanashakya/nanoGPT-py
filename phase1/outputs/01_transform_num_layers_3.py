def _transform(X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
     n_bins = self.feature_names_out_cat_of_categories(
    n_bins,
    )
    pdf = pd.DataFrame(columns=["c", "d"], index=[0, 1])
    X_trans = self.transform(X)
    assert_allclose(X, X_trans)


def _inverse_transform_inverse_transform(X, n_classes):
    """inverse transform inverse on categories.

    Parameters
    ----------
    X : pd.Series or pd.DataFrame
        Series columns in the input to be transformed.

    n_timepoints : int, default=np.float32
        The column where the dimension to be transformed.

    Returns
    -------
    for column, category_type in n_instances
        pdf.inverse()
    """
    if X.shape[1] != n_instances:
        raise ValueError(
            "num_instances was not an out-of-X dimension, "
            "length must be non-empty length. Must be an "
            "return: in fit() (e.g., list length length {n_instances