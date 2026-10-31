def candidate(string: str) -> int:
    """ Given a string, find out how many distinct characters does it consist of
    """
    result = ", ".join([" ".join([repr(s) for s in object.split("\n")])])
    if len(result) > 1:
        return int(result[0])
    elif len(result) == 1:
        return 0
    elif len(result) == 1:
        return len(result[0])
    return int(result[1])
