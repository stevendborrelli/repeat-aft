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
in with pkgs; python3Packages.buildPythonPackage rec {
  pname = "repeat";
  version = "0.1.0";
  name = "repeat-${version}";

  src = ./.;

  # The checkInputs attribute is cleared or deleted or something by
  # buildPythonPackage, so we need a dummy attribute to reference from shell.nix.
  check_inputs = with python3Packages; [ faker factory_boy ];
  checkInputs = check_inputs;

  propagatedBuildInputs = with python3Packages; [
    (callWithPy ./nix/deps/django-polymorphic.nix {django = django;})
    (callWithPy ./nix/deps/django-jsonfield.nix {django = django;})
    (callWithPy ./nix/deps/coreapi.nix {
      requests = requests;
      uritemplate = uritemplate;

      coreschema = callWithPy ./nix/deps/coreschema.nix { jinja2 = jinja2; };
      itypes = callWithPy ./nix/deps/itypes.nix { };
    })
    djangorestframework
    pluginbase
    nltk
    xpdf # scrape text from PDFs
  ];

  NLTK_DATA = (callPackage ./nix/deps/nltk-data/punkt.nix { });

  # Include static CSS files from Django REST framework and Django Admin
  postInstall = ''
    python repeat/manage.py collectstatic --no-input
    mv static/ $out/static/
  '';

  meta = with lib; {
    homepage = https://github.com/ripeta/repeat-aft;
    description = "";
    maintainers = with maintainers; [ siddharthist ];
    platforms = platforms.linux;
  };
}
