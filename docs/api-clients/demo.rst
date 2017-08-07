.. _demo:

Demo
====

Installing Requirements
-----------------------

This project uses `Nix <http://nixos.org/nix/>`_ to manage its dependencies.
Please install that first, and it will handle the rest.

Linux
^^^^^

Now, let's build the project and run the tests:

.. code-block:: shell

    nix-shell        # drop into a shell with all dependencies installed
    ./setup.py test  # run unit tests, just in case
    nix-build        # build
    ls ./result

OSX
^^^

Unfortunately, `Nix <http://nixos.org/nix/>`_ currently
`cannot install a dependency of Django on
OSX <https://github.com/NixOS/nixpkgs/issues/18194>`_. Therefore, we cannot use
it to manage our Python packages. Instead, first install Python, ``pip3``, and
``virtualenv``:

.. code-block:: shell

    nix-env -i python36 python36Packages.pip python36Packages.virtualenv

To isolate the dependencies from your system Python installation, we'll create
and enter a `Virtual
Environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_:

.. code-block:: shell

    virtualenv env
    source env/bin/activate

Download all the required packages and some data from the NLTK project:

.. code-block:: shell

    pip3 install -r requirements.txt  # install Python packages
    python3 -m nltk.downloader punkt  # install an NLTK corpus

Let's build the project and run the tests:

.. code-block:: shell

    ./setup.py test                   # run unit tests
    ./setup.py build                  # build

Running the Server
------------------

.. _local:

Locally
^^^^^^^

To run Django locally, run

.. code-block:: shell

    ./repeat/reset.sh               # set up the database
    ./repeat/manage.py runserver &  # "&" means "run in the background"
    ip=localhost:8000
    url=$ip/api/v0

and proceed to the section :ref:`queries`.

.. _virtual-machine:

On a Virtual Machine
^^^^^^^^^^^^^^^^^^^^

To get the server running on a `virtual machine
<https://en.wikipedia.org/wiki/Virtual_machine>`_ will require
`VirtualBox <https://www.virtualbox.org/>`_. Then:

.. code-block:: shell

    nix-env -i nixops     # we use NixOps to deploy to Virtualbox
    bash ./scripts/vm.sh

If you see any confirmation dialogs, just say "yes". At the end of the log, you
should see an IP address. You can navigate to the address in your web browser,
and you should recieve a 404 page. Now, we can start playing with the API!
Save the IP address as follows and proceed to the section :ref:`queries`:

.. code-block:: shell

    ip=xxx.xxx.xxx.xxx # replace xxx with the appropriate value
    url=$ip/api/v0


.. _queries:

Queries
-------

Let's look at some queries:

.. code-block:: shell

    curl --silent $url/domains
    curl -s $url/categories
    curl -s $url/variables
    curl -s $url/papers

There's not much in there! Let's make a new ``Domain``, and a ``Category``:

.. code-block:: shell

  curl -s --header 'Content-Type:application/json' \
          --data '{"name":"core","description":"whatever"}' $url/domains
  curl -s $url/domains

  curl -sH 'Content-Type:application/json' \
       -d '{"name":"core","description":"des","order":0}' $url/categories
  curl -s $url/categories

If you're wondering what the JSON should look like, you can go ahead and point
your browser to ``http://$url/domains`` (replacing ``$ip`` with the actual
value, of course) to browse the interactive documentation for this API endpoint.

It's unpleasant to write all this JSON right in the shell. To define a variable,
let's first create a file ``funding.json``:

.. literalinclude:: funding.json
   :language: json

Then we can upload it as the data of our request:

.. code-block:: shell

    curl -sH 'Content-Type:application/json' -d '@funding.json' $url/variables

If you get an error about required fields, make sure you entered the correct
path to your ``funding.json`` file after the ``@``.

Finally, if we download the PDF of an
`open-access paper <http://www.nejm.org/doi/pdf/10.1056/NEJMoa1408868>`_, we can
upload a paper. This works a little differently, since we have to include the
file:

.. code-block:: shell

    curl -F 'domains=core' \
         -F 'unique_id=doi:abc' \
         -F 'title=Combined vemurafenib and cobimetinib in ...' \
         -F 'authors=["Author One", "Another Author"]' \
         -F 'document=@paper.pdf' \
         $url/papers

Remember to replace ``paper.pdf`` with the path to a PDF file you'd like to
upload. Now we've got the gist of it. Let's see if we can extract some
information from the paper...

.. code-block:: shell

    curl -s $url/extract/doi%3Aabc/funding
