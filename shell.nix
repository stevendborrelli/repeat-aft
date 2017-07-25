# -*- mode: nix -*-
{ pkgs ? import ./nix/pinned-pkgs.nix { } }:

# To use: run `nix-shell` or `nix-shell --run "exec zsh"`
# https://nixos.org/wiki/Development_Environments
# http://nixos.org/nix/manual/#sec-nix-shell

let
  self = pkgs.callPackage ./default.nix { };
  # Unstable. Required for pre-commit, for flake8 and pycodestyle
  new_pkgs = import (pkgs.fetchFromGitHub {
    owner  = "NixOS";
    repo   = "nixpkgs-channels";
    rev    = "53281023253de9962d9b99b900690f194719c7c2";
    sha256 = "1wmwf58m6y1gz97c64hbk4pw52rwc27hvrsgnr476s4g1n3i0zgz";
  }) { };

  callPackage = pkgs.lib.callPackageWith (pkgs.python3Packages // pkgs);
in with pkgs; with pkgs.python3Packages; buildPythonPackage {
  name = self.name;

  NLTK_DATA = self.NLTK_DATA;

  buildInputs = self.check_inputs ++ self.propagatedBuildInputs ++ [
    git

    # Documentation
    sphinx

    # Development
    autopep8
    coverage
    setuptools
    new_pkgs.python35Packages.flake8
    new_pkgs.python35Packages.pycodestyle
    (callPackage ./nix/deps/pre-commit.nix {
      aspy_yaml = callPackage ./nix/deps/aspy-yaml.nix { };
      identify = callPackage ./nix/deps/identify.nix { };
      nodeenv = callPackage ./nix/deps/nodeenv.nix { };
    })  # http://pre-commit.com/
    yapf        # automatically format source code

    # Only install virtualbox if we're not in Travis, it's a little heavy
  ] ++ (if builtins.getEnv "CI" == "" then [ virtualbox ] else []);
}
