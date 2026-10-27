def check_documents_type(documents):
    """Check whether the input documents are indeed a list of strings."""
    if isinstance(documents, pd.DataFrame):
        raise TypeError("Make sure to supply a list of strings, not a dataframe.")
    elif isinstance(documents, Iterable) and not isinstance(documents, str):
        if not any([isinstance(doc, str) for doc in documents]):
            raise TypeError("Make sure that the iterable only contains strings.")
    else:
        raise TypeError("Make sure that the documents variable is an iterable containing strings only.")