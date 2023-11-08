
import sys
import yaml


def read_yaml_file(sFileName):
    '''
    Attempts to read the suppression file and return an list of rules.

    Parameters:

       sFileName : (String)

    Returns:  dictionary
    '''
    try:
        with open(sFileName) as yaml_file:
            dReturn = yaml.full_load(yaml_file)
    except Exception as e:
        print(e)
        sys.exit(1)

    if dReturn is None:
        dReturn = {}

    return dReturn
