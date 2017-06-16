#!/usr/bin/env bash
set -e

echo "Validating data dictionaries against JSON schema"
cd dictionaries
for json_file in samples/*.json; do
  echo "Validating $json_file"
  jsonschema -i "$json_file" dictionary.schema
done

echo "TODO: non-examples of schema"

echo "Building documentation..."
make -C ../docs html

echo "Done!"
