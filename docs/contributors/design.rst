.. _design:

Design Documentation
====================

.. _plugins:

Plugins
-------

Many variables can automatically be extracted from the source document. For
instance, to figure out whether or not a researcher used Python or R to analyze
their data, we can simply search for "Python" or "R" within the text of the
paper. The relevant variables and how to extract them depend on which
domains are present. We implement the extraction of variables via a plugin
system.

Before deploying, extra plugins can be added to ``repeat/api/analysis/plugins``,
with names corresponding to the name of the variable they extract. See that
directory for examples.

.. _database:

Database
--------

The backend uses Django to manage the database. Thanks to Django, the source
code is actually very readable. If you're new to Django, a ``Model`` corresponds
roughly to a table in a database. We're using a multi-table inheritance strategy
(we have a short hierarchy of ``Variable`` subclasses). The ``help_text``
argument of a field describes what the field should contain.
