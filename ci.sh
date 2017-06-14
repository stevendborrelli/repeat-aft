#!/usr/bin/env bash
set -e

echo "Validating data dictionaries against JSON schema"
cd dictionaries
for json_file in *.json; do
  jsonschema -i "$json_file" dictionary.schema
done

echo "Done!"
