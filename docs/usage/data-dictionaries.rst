Data Dictionaries
=================

The user must select one of several subfields their paper belongs to. Each of
these subfields has certain relevant variables/questions, which are described in
a "data dictionary". These dictionaries are JSON files that describe

..
  TODO document what branching logic is

 * a unique field ID,
 * what type of field it is,
 * what category it falls under,
 * how to ask the user to specify the value,
 * possible field options,
 * (optional) branching logic, 
 * and miscellaneous notes to show the user.

There is a full `JSON schema
<http://github.com/ripeta/repeat-aft/tree/master/dictionaries/dictionary.schema.json>`_
which describes the valid fields in a data dictionary file. The Electronic
Health Record and core dictionaries serve as examples. The variables in the core
dictionary are used regardless of subfield.
