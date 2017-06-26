# -*- mode: nix -*-
{ pkgs ? import ./nix/pinned-pkgs.nix { } }:
# { lib, callPackage, python3Packages }:

with pkgs; with python3Packages; buildPythonPackage {
  name = "repeat-aft";
  src = ./.;
  propagatedBuildInputs = [
    (callPackage ./nix/deps/django-polymorphic.nix {
      buildPythonPackage = buildPythonPackage;
      fetchPypi = fetchPypi;
      django = django;
    })
    (callPackage ./nix/deps/coreapi.nix {
      buildPythonPackage = buildPythonPackage;
      fetchPypi = fetchPypi;
      requests = requests;
      uritemplate = uritemplate;

      coreschema = callPackage ./nix/deps/coreschema.nix {
        buildPythonPackage = buildPythonPackage;
        fetchPypi = fetchPypi;
        jinja2 = jinja2;
      };
      itypes = callPackage ./nix/deps/itypes.nix {
        buildPythonPackage = buildPythonPackage;
        fetchPypi = fetchPypi;
      };
    })
    djangorestframework
    # jsonschema
  ];

  meta = with lib; {
    homepage = https://github.com/ripeta/repeat-aft;
    description = "";
    maintainers = with maintainers; [ siddharthist ];
    platforms = platforms.linux;
  };
}
