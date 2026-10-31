def _transform(X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
    
    # Prior to the X in the training pipeline
    # In this case, we have a column with zero columns (unequal as it for).
    X = X.copy()
    X[:, :, 0] = 0

    # Create the model
    nn_params = None if not isinstance(X, np.ndarray) else dict(X.columns)
    if X.dtypes is not np.object_:
        X = X.copy()

    class DummyFit(Transformer):
        def transform(self, X):
            self.n_instances_, self.n_dims_, self.series_length = X.shape
            return self.components_, X

        def transform(self, X, y=None):
            self.n_instances_, self.series_length = X.shape
            return self.components_, X.shape

        def get_params(self):
            return {}

        def _transform(self, X, y=None):
            return self.transformer_.transform(X)

        def transform(self, X, y=None):
            # TODO: Remove any needed