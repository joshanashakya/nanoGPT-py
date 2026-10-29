def calculate_multilabel_confusion_matrix(target_values, predicted_values, labels) -> pd.DataFrame:
    """
    Calculates a confusion matrix, creates a DataFrame containing values of the confusion matrix, labels and error counts, \
    and returns the DataFrame.
    Args:
        target_values (list of int): List of target value integers.
        predicted_values (list of int): List of predicted value integers.
        labels_map (dict): A dictionary mapping of the label index and label name. e.g. {0: "label1", 1: "label2"}
    Returns:
        pd.DataFrame: A dataframe containing confusion matrix.
        The DataFrame has the following columns:
            - The class labels
            - The number of samples that belong to each class
            - The total number of samples
            - The error count for each label in the confusion matrix
    """

    labels_type = type_maps[indices]

    labels_type = type_maps[target_indices]
    predictions_type = type_maps[predictions_type]
    calibrated_class = calibrated_class.calibrated_class

    predictions = predictions.reshape((-shape, len(metrics_length_of_pred)), (subset_size, _num_samples(predictions_type), 1))

    return predictions
