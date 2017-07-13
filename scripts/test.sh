#!/usr/bin/env bash
set -e

echo ">>> Building documentation..."
rm -rf docs/python/*
nix-shell --no-build-output --run \
          'sphinx-apidoc -o docs/python repeat && \
           make -C ./docs html'

echo ">>> Running nix-build..."
nix-build .

if [[ -z "$CI" ]]; then
  echo ">>> This is not a CI build..."
  echo ">>> Testing building with multiple Python versions..."
  for version in "3.5" "3.6"; do
    echo ">>> Testing Python ${version}..."
    PYTHON_VERSION=$version nix-build
  done
fi

echo ">>> Running coverage.py..."
coverage run --source ./repeat ./setup.py test

coverage report

echo ">>> Done!"
