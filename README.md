# pv-terms
Standard variable names for PV modeling. Formatted documentation available at http://duramat.github.io/pv-terms/

## Building the documentation

To build the documentation locally, you'll need to install the sphinx
requirements.  It's probably a good idea to be working in a virtual
environment, but not strictly necessary. 

    pip install -r requirements.txt

There are a few ways to build the docs. To do this, cd into the `source` folder. The first method generates html files in `source/_build/html`:

    make html

The second method does the same thing but then copies the files into `docs/` so that they'll get detected by Github Pages:

    make github
