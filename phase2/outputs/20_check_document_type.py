def check_documents_type(documents):
    """Check whether the input documents are indeed a list of strings."""
    if isinstance(documents, pd.DataFrame):
    ftype = "f"
    if isinstance(documents, list):
        documents = [
            "f" + doc for doc in documents if doc.values()
            % (documents != ".." or doc.values()) for doc in documents
        ]
    if isinstance(documents, list):
        documents = list(documents)
    if isinstance(documents, list):
        documents = list(documents)
    if len(documents) >= 2:
        raise ValueError(f"No junk document for {documents}!")
    if not documents and delete:
        documents = list(documents)
    if not links:
        documents = [doc for doc in documents]
    documents = [
        "doc_doc" + doc for doc in documents]
    if documents and delete
