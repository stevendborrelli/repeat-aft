# -*- mode: nix -*-
{ pkgs ? import ./nix/pinned-pkgs.nix { } }:

# To use: run `nix-shell` or `nix-shell --run "exec zsh"`
# https://nixos.org/wiki/Development_Environments
# http://nixos.org/nix/manual/#sec-nix-shell

let self = pkgs.callPackage ./default.nix { };
in with pkgs; with pkgs.python3Packages; buildPythonPackage {
  name = self.name;

  NLTK_DATA = self.NLTK_DATA;

  buildInputs = self.check_inputs ++ self.propagatedBuildInputs ++ [
    git

    # Documentation
    sphinx

    # Development
    # autoflake # "SPC m r i" to remove unused imports in Spacemacs
    flake8
    coverage
    pycodestyle
    setuptools
    (callPackage ./nix/deps/pre-commit.nix {
      aspy_yaml = callPackage ./nix/deps/aspy-yaml.nix { };
      identify = callPackage ./nix/deps/identify.nix { };
      nodeenv = callPackage ./nix/deps/nodeenv.nix { };
    })  # http://pre-commit.com/
    yapf        # automatically format source code

    # Only install virtualbox if we're not in Travis, it's a little heavy
  ] ++ (if builtins.getEnv "CI" == "" then [ virtualbox ] else []);
}
