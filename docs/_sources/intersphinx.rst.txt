
Using the Intersphinx mapping
-----------------------------

The `intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
extension makes it easy to create links between sphinx projects.  If you use
sphinx for your project's documentation, you can configure your documentation
to recognize ``pv-terms`` as a linking target by adding an entry to the
``intersphinx_mapping`` dictionary in ``conf.py``:

::

    intersphinx_mapping = {
        'pv-terms': ('https://duramat.github.io/pv-terms/pv-terms/', None),
    }

This lets you write references like this:

::

    Solar position is slightly dependent on site :ref:`pv-terms:elevation`.

that look like this:

    Solar position is slightly dependent on site :ref:`elevation <elevation>`.
