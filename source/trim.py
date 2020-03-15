#!/usr/bin/python
"""
Sphinx HTML output has leading newlines for some reason.  This prevents
GH-Pages from auto-forwarding the root url to index.html, so need to trim out
the leading newlines.  Very easy to do from the shell, but use a python
script in the interest of cross-platform compatibility.

This script removes leading whitespace from the given file (in-place).
"""

import sys

if __name__ == "__main__":

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        contents = f.read()

    with open(filename, 'w') as f:
        f.write(contents.lstrip())
