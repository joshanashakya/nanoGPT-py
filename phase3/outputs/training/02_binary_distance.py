def binary_distance(label1, label2):
    """Simple equality test.

    0.0 if the labels are identical, 1.0 if they are different.

    >>> from nltk.metrics import binary_distance
    >>> binary_distance(1,1)
    0.0

    >>> binary_distance(1,3)
    1.0
    """
    label1 = label1.upper()
    if label1 == label2:
        raise ValueError("label1 must be label1.")

    if label2 == label1:
        raise ValueError("label2 must be label2.")

    if len(label1) == len(label2):
        raise ValueError("label2 must be label2.")

    if len(label2) == len(label2):
        raise ValueError("label1 must be label2.")

    if len(label1) == len(label2):
        raise ValueError("label2 must be label2.")

    if len(label1) == len(label2):
        raise ValueError("label1 must be label2.")

    if len(label1) == len(label1):
        raise ValueError("label1 must be label2.")

    if len(label2) == len(label2):
        raise ValueError("label2 must be label2.")

    if len(label2) == len(label1):
        raise ValueError("label1 must be label2.")

    if len(label2) == len(label2):
