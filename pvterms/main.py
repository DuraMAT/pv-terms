import pandas as pd
import os

# Import pv terms from definitions.csv
_dir_path = os.path.dirname(os.path.realpath(__file__))
_filename_defs = os.path.join(_dir_path, 'definitions.csv')

terms = pd.read_csv(_filename_defs,skiprows=[0,1])
terms.fillna('',inplace=True)

# Make a replacement dictionary
_replacement = {}
for k in terms.index:
    if terms.loc[k,'Deprecated']:
        deprecated_terms = terms.loc[k, 'Deprecated'].split(',')
        standard_term = terms.loc[k, 'Parameter']
        for p in deprecated_terms:
            _replacement[p] = standard_term

def rename(x):
    """
    Rename a variable into the pv-terms scheme. Auto-detect which type of
    renaming scheme to apply.

    Parameters
    ----------
    x : str, dict or dataframe

    Returns
    -------
    renmaed_x
        x with renamed parameters.
    """
    if isinstance(x,type('string')):
        return rename_param(x)
    elif isinstance(x, type(dict())):
        return rename_dict(x)
    elif isinstance(x, type(pd.DataFrame())):
        return rename_dataframe(x)
    else:
        raise Exception("Type {} not allowed".format(type(x)))


def rename_param(parameter):
    """
    Rename a parameter to correspond with pv-terms. If not in the list of
    deprecated parameters, returns input.

    Parameters
    ----------
    parameter : str
        parameter to be changed into pv-terms.

    Returns
    -------
    renamed_parameter : str

    """
    if parameter in _replacement.keys():
        out = _replacement[parameter]
    else:
        out = parameter

    return out



def rename_dict(dictionary):
    """
    Rename keys of a dictionary into the pv-terms scheme.

    Parameters
    ----------
    dictionary : dict
        Dictionary

    Returns
    -------
    renamed_dictionary :
    """
    for key in _replacement.keys():
        if key in dictionary:
            dictionary[_replacement[key]] = dictionary.pop(key)
    return dictionary

def rename_dataframe(df, axis='columns'):
    """
    Rename the column or index of a pandas dataframe to correspond with pv-terms

    Parameters
    ----------
    df : dataframe

    axis : {0 or ‘index’, 1 or ‘columns’}, default 0

    Returns
    -------
    renamed_df
        Renamed dataframe
    """
    return df.rename(mapper=_replacement, axis=axis)
