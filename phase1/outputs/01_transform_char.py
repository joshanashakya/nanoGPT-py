def _transform(X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
    if isinstance(X, pd.Series):
        X = X_encoder.transform(X)
    callable_feature_indices = callable_feature_indices.setdefault(estimator, _int_new
                            func_name, callable_feature_indices)
    X += callable_feature_indices.setdef