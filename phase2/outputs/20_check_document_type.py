def check_documents_type(documents):
    """Check whether the input documents are indeed a list of strings."""
    if isinstance(documents, pd.DataFrame):
    n_features = len(documents)
    documents_type, jit = doclist(documents)
    # In the full case, this only works in a set.
    if n_features == 2:
        doclist = tuple(doclist) + (n_features,)
    elif isinstance(documents_type, pd.Series):
        doclist = tuple(doclist) + (n_features,)
    else:
        raise ValueError("No valid class")

    return doclist
