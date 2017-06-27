# -*- mode: nix -*-
{ pkgs ? import ./nix/pinned-pkgs.nix { } }:
# { lib, callPackage, python3Packages }:

let
  # Curry some common arguments
  # See https://nixos.org/nix/manual/#ch-expression-language
  callWithPy = path: deps: pkgs.callPackage path ({
    buildPythonPackage = pkgs.python3Packages.buildPythonPackage;
    fetchPypi = pkgs.python3Packages.fetchPypi;
  } // deps);
in with pkgs; with python3Packages; buildPythonPackage rec {
  pname = "repeat";
  version = "0.1.0";
  name = "repeat-${version}";

  src = ./.;
  propagatedBuildInputs = [
    (callWithPy ./nix/deps/django-polymorphic.nix {django = django;})
    (callWithPy ./nix/deps/coreapi.nix {
      requests = requests;
      uritemplate = uritemplate;

      coreschema = callWithPy ./nix/deps/coreschema.nix { jinja2 = jinja2; };
      itypes = callWithPy ./nix/deps/itypes.nix { };
    })
    djangorestframework
  ];

  # Include static CSS files from Django REST framework and Django Admin
  postInstall =
    let path = pname: "lib/python3.6/site-packages/${pname}";
    in ''
    mkdir -p "$out/${path pname}/static/"
    cp -r "${djangorestframework}/${path "rest_framework"}/static/rest_framework" \
          "$out/${path pname}/static"
    cp -r "${django}/${path "django"}/contrib/admin/static/admin"\
          "$out/${path pname}/static"
  '';

  meta = with lib; {
    homepage = https://github.com/ripeta/repeat-aft;
    description = "";
    maintainers = with maintainers; [ siddharthist ];
    platforms = platforms.linux;
  };
}
