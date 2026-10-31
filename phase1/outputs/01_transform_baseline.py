def _transform(X) -> pd.DataFrame:
    X = ordinal_encoder.transform(X)
    
    return X, y


@pytest.mark.parametrize(
    ["c_container", ValVectorizer, StratifiedMethods],
    ids=["stratified_func", "stratified_func_is_none"],
)
def test_transform_is_one_of_missing_only_raises_warning() -> None:
    # Test that we are not the error if it is any of its missing path on a missing value.
    msg = r"No valid values \0m1, got in {value}"
    with pytest.raises(TypeError, match=msg):
        DaskCollection()
    with pytest.raises(ValueError, match=msg):
        DaskCollection()


@pytest.mark.parametrize(
    ["c_container", ValVectorizer, StratifiedMethods],
    ids=["stratified_func", "stratified_func_is_none"],
)
def test_transform_is_one_of_missing_raises(c_container: dict) -> None:
    # Test that we are not the error if it is any of its missing path on a