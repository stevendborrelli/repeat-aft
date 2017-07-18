{ lib, buildPythonPackage, fetchPypi,
  # Build dependencies
  aspy_yaml, cached-property, identify, nodeenv, six, virtualenv }:

buildPythonPackage rec {
  pname = "pre_commit";
  version = "0.15.2";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1i2zw8r865lrzkf2d8iqxkjbk05sy22404n0yv6ni7d4i8crzx67";
  };

  doCheck = false;

  propagatedBuildInputs = [
    aspy_yaml
    cached-property
    identify
    nodeenv
    six
    virtualenv
  ];

  meta = {
    homepage = "http://pre-commit.com/";
    description = "A framework for managing and maintaining multi-language pre-commit hooks";
    license = lib.licenses.mit;
  };
}
