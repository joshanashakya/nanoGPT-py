def _transform(self, X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
    if handle_unknown == 'error':
        if X[cols].isin([util.UNKNOWN_SENTINEL]).any().any():
            raise ValueError('Columns to be encoded cannot contain new values')

    X = transform_contrast_coding(X, mapping=mapping)
    return X
