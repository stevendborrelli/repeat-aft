#!/usr/bin/env bash
set -e

if [[ -z "$IN_NIX_SHELL" ]]; then
  nix-shell --run "$0"
  exit $?
fi

echo ">>> Building documentation..."
make -C ./docs html

echo ">>> Running nix-build..."
nix-build

if [[ -z "$CI" ]]; then
  deployment_name="test_deployment"
   echo ">>> This is not a CI build, testing VM deployment"
   nixops info -d "$deployment_name" &> /dev/null \
    && nixops destroy -d "$deployment_name" --confirm \
    && nixops delete -d "$deployment_name"
   nixops create -d "$deployment_name" nix/ops/*
   nixops deploy -d "$deployment_name" --show-trace
   nixops ssh -d "$deployment_name" webserver "systemctl status repeat; systemctl start repeat; journalctl -u repeat"
fi

echo "Done!"
