{ lib, buildPythonPackage, fetchPypi, django }:

# As of 17.09, this is part of nixpkgs:
# https://github.com/NixOS/nixpkgs/pull/26914

buildPythonPackage rec {
  pname = "django-polymorphic";
  version = "1.2";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1bz86711sx2b66rl2xz141xppsfmlxilkgjgq0jsavpw37vg7r3r";
  };

  checkInputs = [ django ];
  propagatedBuildInputs = [ django ];

  meta = {
    homepage = "https://github.com/django-polymorphic/django-polymorphic";
    description = "Improved Django model inheritance with automatic downcasting";
    license = lib.licenses.bsd3;
  };
}
