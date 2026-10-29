def candidate(string: str) -> int:
    """ Given a string, find out how many distinct characters does it consist of
    """
    with pytest.raises(TypeError, match=msg):
        candidate = string.ascii_pars(input)
