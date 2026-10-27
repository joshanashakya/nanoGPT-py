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

    # create confusion matrix of the prediction
    c_matrix = multilabel_confusion_matrix(target_values, predicted_values, labels=labels)

    # add label names as the columns of the confusion matrix dataframe
    c_matrix_df = pd.DataFrame(c_matrix, columns=labels)

    # add support count of the labels
    c_matrix_df["total"] = c_matrix_df.sum(axis=1)

    # add labels as to the label column of the dataframe
    c_matrix_df["label"] = label_values

    # calculate error count
    c_matrix_w_error_df = calculate_confusion_matrix_error(c_matrix_df)

    return c_matrix_w_error_df