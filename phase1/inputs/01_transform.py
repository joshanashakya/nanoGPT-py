def _transform(X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
    