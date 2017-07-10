#!/usr/bin/env bash
set -e

# Destroy the virtual machines
function destroy {
  if nixops info -d "$deployment_name" &> /dev/null; then
    nixops destroy -d "$deployment_name" --confirm
    nixops delete -d "$deployment_name"
  fi
}

# Run some basic tests to see if some static files are present
function curl_tests {
  curl "$1:80" > /dev/null
  curl "$1:80/static/admin/css/login.css" > /dev/null
  curl "$1:80/static/rest_framework/css/default.css" > /dev/null
}

deployment_name="test_deployment"
if [[ "$1" == ssh ]]; then
  nixops ssh -d "$test_deployment" webserver; exit $?

## Cleanup

elif [[ "$1" == destroy ]]; then destroy; exit $? ; fi

echo ">>> Testing VM deployment"
destroy
nixops create -d "$deployment_name" nix/ops/{logical.nix,vbox.nix}
nixops deploy -d "$deployment_name" --show-trace

# If the deployment failed, show logs
ip=$(nixops info -d "$deployment_name" --plain | awk '{print $5}')
nixops ssh -d "$deployment_name" webserver "systemctl start repeat"
sleep 1
if ! (curl_tests "$ip" > /dev/null); then
  nixops ssh -d "$deployment_name" webserver "systemctl start repeat"
fi
if ! (curl_tests "$ip") > /dev/null; then
  nixops ssh -d "$deployment_name" webserver "journalctl -u repeat"
  exit 1
fi
echo ">>> IP address: $ip"

echo ">>> Done!"
