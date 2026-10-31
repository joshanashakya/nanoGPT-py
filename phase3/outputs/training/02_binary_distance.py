def binary_distance(label1, label2):
    """Simple equality test.

    0.0 if the labels are identical, 1.0 if they are different.

    >>> from nltk.metrics import binary_distance
    >>> binary_distance(1,1)
    0.0

    >>> binary_distance(1,3)
    1.0
    """
    result = binary_distance(label1, label2)

    if not issubclass(label2, label2):
        raise ValueError(f"Invalid label type: {label2}")

    # Only raise an error.
    if label == 0.0:
        # If the labels are expected, a label 1-0, and the labels are
        # expected.
        if label is not None and label != 1.0:
            raise ValueError(f"Invalid label type: {label}")

        # If the labels are expected, a label >= 1.0, which
        if label == 1.0:
            result.append(label)
        else:
            # If label is expected, one
            if label == 1.0:
                result.append(
                    label)
        result.append(
            )
        if label != 0.0:
            raise ValueError(f"Invalid label type: {label}")

    else:
        result.append(
            [str(t) for t in label]
        )
        # Return a list of (label, label) pairs where each label is a tuple
