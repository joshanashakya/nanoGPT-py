    def _prepare_data(self, labels_map) -> pd.DataFrame:
        """
        Prepares the dataframe from the data_path by using labels_map.
        Args:
            labels_map (dict): A dictionary mapping of the label index and label name. e.g. {0: "label1", 1: "label2"}
        Returns:
            pd.DataFrame: A DataFrame containing different columns based on the different conditions:
                Condition 1: Multiple Tags Configuration
                    - submission_id: The submission id of the feedback.
                    - feedback: The feedback string.
                    - multilabel: The multilabel present in the input dataset.
                    - multitarget: A string containing the integer value of the labels separated by comma.
                    - target: The true target integer value of the label.
                If the "multilabel" column is not present in the dataframe read from the data_path, then the returned DataFrame
                has only "submission_id" and "feedback" columns.

                Condition 2: Single Tag Configuration
                    - submission_id: The submission id of the feedback.
                    - feedback: The feedback string.
                    - label: The true label of the feedback.
                    - target: The true target integer value of the label.
                    - multilabel: The multilabel present in the input dataset.
                If the dataframe in the data_path has "label" and "multilabel" columns, then the dataframe have all the
                columns. Else if the dataframe has "label" column, then the dataframe will have all the columns except
                "multilabel" column. Otherwise, the dataframe will have only the "submission_id" and "feedback" columns.
        """
