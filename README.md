# RepeAT Automator

[![Documentation Status](https://readthedocs.org/projects/repeat-aft/badge/?version=latest)](http://repeat-aft.readthedocs.io/en/latest/?badge=latest)

The RepeAT automator is a tool for improving reproducibility in the biomedical
sciences. It builds on a systematic review of best practices in research
reproducibility, producing partially automated analyses of papers.

## Background

In collaboration with the Washington University Center for Biomedical
Informatics and the Washington University library, [ripeta][ripeta] conducted
literature reviews and interviews with biomedical researchers to understand best
practices for research reproducibility. From this knowledge, we synthesized a
framework for analyzing papers and operationalized it in the form of this
program.

## Description

This repository holds the backend to a program that implements the mentioned
framework. Researchers and publishers will upload papers, and this backend will
extract what variables it can, and users will fill in the rest via a web UI. The
results are presented to the user in a simple dashboard.
The [frontend][frontend] documentation has more details on the UI.

## Documentation

Please refer to [the documentation][docs] for further description of the project.

The design, usage, and Python API documentation is provided via [Sphinx][sphinx]
and hosted on [Read the Docs][readthedocs]. The JSON API documentation is done
via [Swagger][swagger] (in the future, it will hopefully be automatically build
in Travis CI and hosted on Github pages).
   
[ripeta]: http://www.ripeta.com/
[frontend]: https://github.com/ripeta/repeat-frontend
[docs]: http://repeat-aft.readthedocs.io/en/latest/?badge=latest
[sphinx]: http://www.sphinx-doc.org/en/stable/
[readthedocs]: http://www.readthedocs.org
[swagger]: http://swagger.io/
