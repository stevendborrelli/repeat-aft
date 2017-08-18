.. _administrators:

Administrators
==============

Deploying
---------

There are currently only two options for deploying the server: :ref:`local` and
:ref:`virtual-machine`. Both are covered in :ref:`demo`. The :ref:`roadmap`
includes more deployment options, specifically to a cloud provider.

Making changes to the database
------------------------------

There are three ways to make changes to the contents of the database. The
recommended way to do so is to add your new domain/category/variable to the file
``repeat/api/fixtures/fixture.json``. These changes will be applied every time
the server is booted.

There is a Django administrative interface. You can navigate your browser to
``<hostname or ip>:<port>/admin``, and make changes there.

You can also interact with the API as a client would (:ref:`api-clients`), as
demonstrated in the :ref:`demo`. These changes will not persist across reboots
(although this feature is planned: :ref:`roadmap`).


Automatically extracting new variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a Python plugin to extract your new variable please see the documentation
on plugins: :ref:`plugins`.
