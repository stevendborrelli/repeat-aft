.. _branching-logic:

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

.. include:: ../../json/samples/skip-simple.json
   :literal:

Atomic statements can be combined using ``and``, ``or`` and ``not`` operators to
form `compound` statements. These operators can be nested arbitrarily. Both
``and`` and ``or`` take lists of statements (atomic, compound, or a mix of both)
as inputs, whereas ``not`` takes a single statement as input.

.. include:: ../../json/samples/skip-complex.json
   :literal:
