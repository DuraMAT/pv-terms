import pandas as pd
import os

# Import pv terms from definitions.csv
_dir_path = os.path.dirname(os.path.realpath(__file__))
_filename_defs = os.path.join(_dir_path, 'definitions.csv')

terms = pd.read_csv(_filename_defs,skiprows=[0,1])
terms.fillna('',inplace=True)

# Make a replacement dictionary
replacement = {}
for k in terms.index:
    if terms.loc[k,'Deprecated']:
        deprecated_terms = terms.loc[k, 'Deprecated'].split(',')
        standard_term = terms.loc[k, 'Parameter']
        for p in deprecated_terms:
            replacement[p] = standard_term
