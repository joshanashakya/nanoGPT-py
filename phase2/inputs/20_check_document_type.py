def check_documents_type(documents):
    """Check whether the input documents are indeed a list of strings."""
    if isinstance(documents, pd.DataFrame):
   