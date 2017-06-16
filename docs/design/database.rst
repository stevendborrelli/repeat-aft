.. _database:

Database
--------

The backend uses Django to manage the database. Thanks to Django, the source
code is actually very readable. If you're new to Django, a ``Model`` corresponds
roughly to a table in a database. We're using a multi-table inheritance strategy
(we have a short hierarchy of ``Variable`` subclasses). The ``help_text``
argument of a field describes what the field should contain.

.. The ``Variable`` class is an abstract base class, which means that every
   subclass of ``Variable`` gets its own database table. However, since
   ``ForeignKey`` can only reference one other kind of model, we use the
   ``contenttypes`` Django plugin to allow ``Values`` to reference any subclass of
   ``Variable``.

.. include:: ../../repeat/api/models.py
   :literal:

These entities and their relationships are summarized in the following
entity-relationship diagram:

.. TODO: diagram
