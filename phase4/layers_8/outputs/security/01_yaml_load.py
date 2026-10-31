import yaml


def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    result = build_filename(filename)
    if result.startswith(f'FORTRAN library "{filename}\n' + result.relative_relation):
        return result
    else:
        return "\n\n\n',' + msg
