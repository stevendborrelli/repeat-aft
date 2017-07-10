#!/usr/bin/env bash
set -e

echo ">>> Building documentation..."
nix-shell --no-build-output --run 'make -C ./docs html'

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

echo ">>> Done!"
