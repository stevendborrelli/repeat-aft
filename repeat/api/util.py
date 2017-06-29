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

import subprocess
import tempfile

def pdf_to_text(data):
    """ Convert PDF data to a string """
    temp = tempfile.NamedTemporaryFile()
    temp.write(data)
    text = pdf_file_to_text(temp.name)
    temp.close()
    return text

def pdf_file_to_text(filename):
    """ Extract text from PDFs using the pdftotext command line utility """
    completed = subprocess.run(["pdftotext", "-enc", "UTF-8", filename, "-"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    completed.check_returncode()
    return completed.stdout.decode("utf8", "ignore")
