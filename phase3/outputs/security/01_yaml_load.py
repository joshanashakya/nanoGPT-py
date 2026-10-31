import yaml


def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    """
    header = os.path.join(filename, filename)
    if not header:
        raise ValueError('Found a file and has a file handle')
    errors.add(header)
    return header.getvalue()
