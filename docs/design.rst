Design Documentation
====================

REST JSON API
-------------

The JSON API is constructed using `Django <https://www.djangoproject.com/>`_ and
the `Django REST Framework <http://django-rest-framework.org/>`_. 

.. TODO: documentation, swagger?

Plugins
-------

Many variables can automatically be extracted from the source document. For
instance, to figure out whether or not a researcher used Python or R to analyze
their data, we can simply search for "Python" or "R" within the text of the
paper. The relevant variables and how to extract them depend on which 
domains are present. Thus, we implement the extraction of variables via a plugin
system.

.. TODO: make this true

The backend takes a ``--plugin-dir`` argument which specifies where to search
for these plugins. By default, the search path is ``./repeat/plugins``. 
If you have a plugin to extract a ``Variable`` with ID ``example_variable``, it
should be located at ``<plugin-dir>/example_variable.py``

.. TODO: example plugins
