Data Dictionaries
=================

The user must select one of several subfields their paper belongs to. Each of
these subfields has certain relevant variables/questions, which are described in
a "data dictionary". These dictionaries are `JSON <http://json.org/>`_ files
that describe

 * a unique field ID,
 * what type of field it is,
 * what category it falls under,
 * how to ask the user to specify the value,
 * possible field options,
 * (optional) branching logic, 
 * (optional) validation logic, 
 * and miscellaneous notes to show the user.

.. TODO: link to examples

The Electronic Health Record and core dictionaries serve as examples. The
variables in the core dictionary are used regardless of subfield.

Branching Logic
---------------

Branching or skip logic describes whether or not a question/variable is still
relevant in the presence of another answer. For instance, if the user states
that no database is used in their study, then we need not ask them about whether
or not their database is open source.

The simplest statement is of the form
``{ "field_id": "some_field_id", "value": "some_value" }``, which states
that we require the value of ``some_field_id`` to be ``"some_value"`` in order
to ask the current question. Such statements are called `atomic`. For example,
this dictionary can be read as "Only ask ``question2`` if the answer to
``question1`` is ``true``":

.. include:: ../../dictionaries/samples/skip-simple.json
   :literal:

Atomic statements can be combined using ``and``, ``or`` and ``not`` operators to
form `compound` statements. These operators can be nested arbitrarily. Both
``and`` and ``or`` take lists of statements (atomic, compound, or a mix of both)
as inputs, whereas ``not`` takes a single statement as input.

.. include:: ../../dictionaries/samples/skip-complex.json
   :literal:


Schema
------

This `JSON schema <http://json-schema.org/>`_ is a formal, machine- and human-
readable description of the valid objects of a data dictionary file. It is
available `on Github
<http://github.com/ripeta/repeat-aft/tree/master/dictionaries/dictionary.schema>`_,
and is reproduced below.

.. include:: ../../dictionaries/dictionary.schema
   :literal:
