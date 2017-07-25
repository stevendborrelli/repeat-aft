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
  # pyPkgs =
  #   let val = builtins.getEnv "PYTHON_VERSION";
  #   in versionMap . "${val}" or python3Packages;

  pyPkgs = python3Packages;

  # callPackage should fill in both Python and non-python arguments
  callPackage = pkgs.lib.callPackageWith (pyPkgs // pkgs);

  # Needs to be used in factory_boy definition
  faker_07 = callPackage ./nix/deps/faker.nix {
    email_validator = callPackage ./nix/deps/email-validator.nix {
      dns = callPackage ./nix/deps/dns.nix { };
    };
    ukpostcodeparser = callPackage ./nix/deps/ukpostcodeparser.nix { };
  };

in with pyPkgs; callPackage ./nix/repeat.nix {
  django-jsonfield = callPackage ./nix/deps/django-jsonfield.nix { };
  django-polymorphic = callPackage ./nix/deps/django-polymorphic.nix { };
  djangorestframework = callPackage ./nix/deps/djangorestframework.nix { };
  factory_boy = callPackage ./nix/deps/factory-boy.nix { faker = faker_07; };
  faker = faker_07;
  nltk = callPackage ./nix/deps/nltk.nix { };
  pluginbase = callPackage ./nix/deps/pluginbase.nix { };
  punkt = callPackage ./nix/deps/nltk-data/punkt.nix { };
  # coreapi = callPackage ./nix/deps/coreapi.nix {
  #     coreschema = callPackage ./nix/deps/coreschema.nix { };
  #     itypes = callPackage ./nix/deps/itypes.nix { };
  # };
}
