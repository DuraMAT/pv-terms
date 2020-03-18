"""
A preprocessing stage that generates RST lists from the definitions CSV file.
"""

import pandas as pd
import os
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


def generate_bullet_list(terms, definitions, alternates):
    """
    Generate a chunk of RST with a list of bullets containing the
    supplied definitions.  Terms and definitions can include RST formatting
    like math formulas.  A reference is automatically inserted for each term
    so that it can be referenced externally via intersphinx.

    Parameters
    ----------
    terms : list
    definitions : list
    alternates : list

    Returns
    -------
    str
        The RST glossary text
    """
    lines = []
    for term, definition, alternate in zip(terms, definitions, alternates):
        # it's a little tricky to get RST labels to not interfere with
        # bulleted list formatting.  What works is to do it like this:

        #   .. _dc:
        #
        # * **dc**: direct current
        #
        #   .. _ac:
        #
        # * **ac**: alternating current

        alt = " (*{}*)".format(alternate) if alternate else ''

        list_entry = (
            "\n"
            "  .. _{}:\n"  # label (invisible)
            "\n"
            "* **{}**{}: {}".format(term, term, alt, definition)
        )
        lines.append(list_entry)
    return "\n".join(lines)


if __name__ == "__main__":
    df = pd.read_csv("../definitions.csv")
    df = df.fillna('')

    grouper = df.groupby('Category')

    for category in grouper.groups:
        subset = grouper.get_group(category)
        terms = subset['Parameter']
        definitions = subset['Description']
        alternates = subset['Deprecated']
        rst = generate_bullet_list(terms, definitions, alternates)

        filename = category.lower().replace(" ", "-") + ".rst"
        filename = os.path.join('.', 'generated', filename)
        with open(filename, "w") as f:
            f.write(rst)
