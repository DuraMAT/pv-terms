About pv-terms
--------------

The pv-terms project standardizes the nomenclature used for photovoltaic (PV) system modeling. A uniform standard for the PV modeling community enables compatibility within and between software packages and data sources. 

The nomenclature was designed with the following criteria:

- Emphasize clarity. E.g. temperature_cell is better than temp_cell.
- Write out most variables rather than use abbreviations. E.g. use num_cells_in_series rather than N_s.
- Style: No spaces or special characters, but underscores are okay. Most variables are commpletely lower case and separated by underscores
- Use common PV abbreviations, e.g. ac, dc, poa, mp, etc.
- Organize some variables "taxonomy style" (e.g temperature_cell) and others "human-readable style" (e.g. solar_zenith). It is not necessary to conform all variables to a single style
- Variables have a defined unit. e.g. W/m^2 for irradiance. 