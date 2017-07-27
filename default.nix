# -*- mode: nix -*-
{ pkgs ? import ./nix/pinned-pkgs.nix { } }:

# You can pick a Python version to build with by setting e.g. PYTHON_VERSION=3.5
with pkgs; let
  versionMap = {
    "3.3" = python33Packages;
    "3.4" = python34Packages;
    "3.5" = python35Packages;
    "3.6" = python36Packages;
    "pypy" = pypyPackages;
  };
  pyPkgs =
    let val = builtins.getEnv "PYTHON_VERSION";
    in versionMap . "${val}" or python3Packages;
in with pyPkgs; callPackage ./nix/repeat.nix {
  django-polymorphic = callPackage ./nix/deps/django-polymorphic.nix { };
  django-jsonfield = callPackage ./nix/deps/django-jsonfield.nix { };
  django-registration = callPackage ./nix/deps/django-registration.nix { };
  punkt = callPackage ./nix/deps/nltk-data/punkt.nix { };
  # coreapi = callPackage ./nix/deps/coreapi.nix {
  #     coreschema = callPackage ./nix/deps/coreschema.nix { };
  #     itypes = callPackage ./nix/deps/itypes.nix { };
  # };
}
