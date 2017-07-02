{ lib, buildPythonPackage, fetchPypi, django }:

buildPythonPackage rec {
  pname = "jsonfield";
  version = "2.0.2";
  name = "django-${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "0d5qmjja31rgcj524qy8x527fx81dj1cpvys68f3bmnna14cvcdy";
  };

  checkInputs = [ django ];
  propagatedBuildInputs = [ django ];

  meta = {
    homepage = "https://github.com/django-polymorphic/django-polymorphic";
    description = "A reusable JSONField model for Django to store ad-hoc data";
    license = lib.licenses.mit;
  };
}
