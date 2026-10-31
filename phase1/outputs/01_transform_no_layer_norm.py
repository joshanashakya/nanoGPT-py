def _transform(X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
    
    return X, y


def _parallel_transform(X: pd.DataFrame) -> pd.DataFrame:
    X_transformed = X.reset_index(drop=True)


def gen_get_transform():
    X, y = _parallel_transform(X, y, return_X)

    return pd.Series(
        data=X_transformed if return_X_transformed else X, name=_transform(X, y, return_X_transformed=True)
    )


def gen_get_transform():
    X, y = _parallel_transform(X, y, return_X_transformed=True)
    return pd.DataFrame(
        data=X_transformed,
        index=y,
        columns=["x"],
        columns=["h4"],
        columns=["h3"],
        columns=["x3"],
    )


def gen_get_transform_name():
    X, y = _parallel_transform(X, y, return_X_transformed=True)

    return X, X_transformed, name=_transform(X, y, return_X_transformed