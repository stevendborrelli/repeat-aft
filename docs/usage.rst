.. _usage:

Usage Documentation
===================

This project uses `Nix <http://nixos.org/nix/>`_ to manage its dependencies.
Please install that first, and it will handle the rest.

Now, let's build the project and run the tests:

.. code-block:: shell

    nix-shell        # drop into a shell with all dependencies installed
    ./setup.py test  # run unit tests, just in case
    nix-build        # build
    ls ./result

Awesome! The next step is to get the server running on a
`virtual machine <https://en.wikipedia.org/wiki/Virtual_machine>`_. If you
don't have `VirtualBox <https://www.virtualbox.org/>`_ installed, please get it
now. The next part is easy:

.. code-block:: shell

    nix-env -i nixops     # we use NixOps to deploy to Virtualbox
    bash ./scripts/vm.sh

At the end of the log, you should see an IP address. You can navigate to the
address in your web browser, and you should recieve a 404 page. Now, we can
start playing with the API!

.. code-block:: shell

    ip=xxx.xxx.xxx.xxx # replace xxx with the appropriate value
    url=$ip/api/v0
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
