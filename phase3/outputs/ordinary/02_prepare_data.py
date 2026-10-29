def _prepare_data(labels_map):
    """
    Prepares the dataframe from the data_path by using labels_map.
    Args:
        labels_map (dict): A dictionary mapping of the label index and label name. e.g. {0: "label1", 1: "label2"}
    Returns:
        pd.DataFrame: A DataFrame containing different columns based on the different conditions:
    """
    _check_plot_works(data_path, labels_map, labels_map, **kwargs)
