.. _index:

repeat-aft documentation
========================

The RepeAT automator is a tool for improving reproducibility in biomedical
research. It builds on a systematic review of best practices in research
reproducibility, producing partially automated analyses of papers.

Please see `the README <https://github.com/ripeta/repeat-aft>`_ for a high-level
description of this project.

Documentation structure
-----------------------

This documentation is structured based on the reader's role in the project.
The :ref:`concepts` documentation covers basic concepts and vocabulary, and
will be useful to almost all readers.

 * Administrators: those who will be running and maintaining instances of the
   software on servers
 * Contributors: people interested in adding code to the backend (also some
   design concepts that may be useful to front-end developers)
 * API Clients: people interested in using the API directly programmatically
   (including front-end developers), or manually with ``curl``.

.. toctree::
   :caption: Contents:
   :maxdepth: 2

   concepts

   administrators
   administrators/security
   administrators/branching-logic

   contributors
   contributors/design
   contributors/python

   api-clients
   api-clients/demo

   roadmap
