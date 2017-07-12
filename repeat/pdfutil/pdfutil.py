# The MIT License (MIT)

# Copyright (c) 2014 Dean Malmgren

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
""" Utilities to extract strings from PDFs """

import logging
import subprocess
import tempfile

logger = logging.getLogger(__name__)


def pdf_to_text(data, logger=logger):
    """ Convert PDF data to a string

    Simply creates a temporary file and calls ``pdf_file_to_text``

    Args:
        data: The data, as bytes, of a PDF file
        logger: An instance of Python's standard logging class

    Returns:
        The text contained in the PDF file, as a string

    Raises:
        See ``pdf_file_to_text``
    """
    temp = tempfile.NamedTemporaryFile(delete=False)
    with temp as f:
        temp.write(data)

    return pdf_file_to_text(temp.name, logger=logger)


def pdf_file_to_text(filename, logger=logger):
    """ Extract text from PDFs using the pdftotext command line utility

    Args:
        filename: The path to the PDF file
        logger: An instance of Python's standard logging class

    Returns:
        The text contained in the PDF file, as a string

    Raises:
        FileNotFoundError: When ``pdftotext`` isn't installed
        subprocess.CalledProcessError: When ``pdftotext`` exits with an error

    Examples:

        >>> import os.path
        >>> pdf_file_to_text(os.path.join(os.path.dirname(__file__), "blank.pdf"))
        '\\x0c'
    """
    completed = subprocess.run(["pdftotext", "-enc", "UTF-8", filename, "-"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    try:
        completed.check_returncode()
    except subprocess.CalledProcessError as e:
        logging.error(e)
        logging.error("code: {}".format(completed.returncode))
        logging.error("stdout: {}".format(completed.stdout))
        logging.error("stderr: {}".format(completed.stderr))
        raise e

    return completed.stdout.decode("utf8", "ignore")
