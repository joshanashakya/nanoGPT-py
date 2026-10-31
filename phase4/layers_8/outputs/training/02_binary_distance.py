def binary_distance(label1, label2):
    """Simple equality test.

    0.0 if the labels are identical, 1.0 if they are different.

    >>> from nltk.metrics import binary_distance
    >>> binary_distance(1,1)
    0.0

    >>> binary_distance(1,3)
    1.0
    """
    result = set("binary_distance", "per_class")
    if not isinstance(result, float):
        raise TypeError("result must be a float or boolean")

    if isinstance(label1, (tuple, list, int)):
        return result
    elif isinstance(label1, tuple):
        return [[], [0])
    else:
        return float(len(labels))
