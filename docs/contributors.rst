.. _contributing:

Contributing
============

Nix
---

As a contributor, you can use `Nix <https://nixos.org/nix/>`_ to manage both
build-time and development requirements. In particular, running ``nix-shell``
will drop you into a terminal with all dependencies available. All commands in
this document assume that you're in the Nix shell.

Sphinx Documentation
--------------------

You can build the documentation with

.. code-block:: shell

   make -C docs html

This builds both the hand-written reStructuredText documentation (e.g. this
page) and the Python API documentation, provided by
`Autodoc <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_.

Testing
-------

To run all Python tests, run

.. code-block:: shell

   python3 setup.py test

from inside the Nix shell. To test with multiple Python versions (not guaranteed
to work), run `Coverage.py <http://coverage.readthedocs.io/>`_, and test the
documentation build, run

.. code-block:: shell

   bash scripts/test.sh

Pre-commit hooks
----------------

This project uses `pre-commit <http://pre-commit.com/>`_ to maintain
high-quality commits. It will run several checks on your changes before allowing
you to commit code, including removing trailing whitespace, checking
JSON/YAML/Python syntax, and others. You'll be all set up with ``pre-commit`` as
soon as you're in the Nix shell.
