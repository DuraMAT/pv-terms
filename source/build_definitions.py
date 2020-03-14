#!/usr/bin/python

import pandas as pd
import datetime

def generate_glossary(terms, definitions, category):
    """
    Generate a chunk of RST with a `glossary` directive containing the
    supplied definitions.  Terms and definitions can include RST formatting
    like math formulas.

    Parameters
    ----------
    terms : list
    definitions : list
    category : str

    Returns
    -------
    str
        The RST glossary text
    """
    indent = "   "
    lines = [".. glossary::", '']
    for term, definition in zip(terms, definitions):
        lines.append(indent + term + " : " + category)
        lines.append(indent*2 + definition)
        lines.append('')
    return "\n".join(lines)


def generate_table(terms, definitions, headers, title):
    """
    Generate a chunk of RST with a `csv-table` directive containing the
    supplied definitions.  Terms and definitions can include RST formatting
    like math formulas.  A reference is automatically inserted for each term
    so that it can be referenced externally via intersphinx.

    Parameters
    ----------
    terms : list
    definitions : list
    headers : list
    title : str

    Returns
    -------
    str
        The RST glossary text
    """
    header = ", ".join('"{}"'.format(h) for h in headers)
    indent = "    "
    lines = [
        ".. csv-table:: " + title,
        indent + ":header: " + header,
        ''
    ]
    for term, definition in zip(terms, definitions):
        row = '".. _{}:\n\n    {}","{}"'.format(term, term, definition)
        lines.append(indent + row)
    return "\n".join(lines)


if __name__ == "__main__":
    df = pd.read_csv("../definitions.csv")

    grouper = df.groupby('Category')

    table_texts = []

    for category in grouper.groups:
        subset = grouper.get_group(category)
        terms = subset['Parameter']
        definitions = subset['Description']
        rst = generate_table(terms, definitions, ['Term', 'Description'],
                             category)
        table_texts.append(rst)

    rst = "\n\n".join(table_texts)

    with open("definitions.rst", "w") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(".. generated on " + timestamp + "\n\n")
        f.write(rst)
