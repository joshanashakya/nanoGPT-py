from typing import List


def candidate(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers meeting a certain condition (e.g. closer to or larger than each other than
    given threshold).
    >>> candidate([1.0, 2.0, 3.0], 0.5)
    False
    >>> candidate([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    return len(support) <= self._thresholds
