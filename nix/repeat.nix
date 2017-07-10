# -*- mode: nix -*-
{
  lib, buildPythonPackage,
  # checkInputs
  faker, factory_boy,
  # propagatedBuildInputs
  djangorestframework, django-polymorphic, django-jsonfield, pluginbase, nltk,
  punkt, xpdf
}:

buildPythonPackage rec {
  pname = "repeat";
  version = "0.1.0";
  name = "repeat-${version}";

  src = ../.;

  # The checkInputs attribute is cleared or deleted or something by
  # buildPythonPackage, so we need a dummy attribute to reference from shell.nix.
  check_inputs = [ faker factory_boy ];
  checkInputs = check_inputs;

  propagatedBuildInputs = [
    djangorestframework
    django-polymorphic
    django-jsonfield
    pluginbase
    nltk
    xpdf # scrape text from PDFs
  ];

  NLTK_DATA = punkt;

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
