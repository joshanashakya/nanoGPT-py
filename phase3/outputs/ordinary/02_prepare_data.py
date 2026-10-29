def _prepare_data(labels_map):
    """
    Prepares the dataframe from the data_path by using labels_map.
    Args:
        labels_map (dict): A dictionary mapping of the label index and label name. e.g. {0: "label1", 1: "label2"}
    Returns:
        pd.DataFrame: A DataFrame containing different columns based on the different conditions:
    """

    labels_map = {}
    for labels_map in labels_map:
        list_map = set(labels_map.keys())
        if not np.iterable(labels.values()):
            raise ValueError(
                "labels_map must be a sequence or list of vectors."
            )

    labels_map = set([labels_map.values() for labels_map in labels_map])

    if isinstance(labels_map, Sequence):
        if len(labels_map) != len(labels):
            raise ValueError(
                "labels_map must be an integer or length-1d"
                " instead of label length-1d."
                f"Expected len(labels_map)={len(labels_map)} tuples"
            )
