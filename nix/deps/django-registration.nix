{ lib, buildPythonPackage, fetchPypi, django }:

buildPythonPackage rec {
  pname = "django-registration";
  version = "2.2";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "10w22xq7hqddxj653dxq911p4xib510s4vh93nmay0nrgb0a9zql";
  };

  checkInputs = [ django ];
  propagatedBuildInputs = [ django ];

  meta = {
    homepage = "https://github.com/ubernostrum/django-registration";
    description = "An extensible user-registration application for Django";
    license = lib.licenses.bsd3;
    platforms = django.meta.platforms;
  };
}
