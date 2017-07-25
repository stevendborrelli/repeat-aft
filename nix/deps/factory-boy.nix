{ lib, buildPythonPackage, fetchPypi, fake_factory, faker }:

buildPythonPackage rec {
  pname = "factory_boy";
  version = "2.8.1";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1fvin6san5xsjh2c4y18caj2lnmwxlylyqm8mh1yc6rp38wlwr56";
  };

  doCheck = false;

  propagatedBuildInputs = [ fake_factory faker ];

  meta = with lib; {
    description = "A Python package to create factories for complex objects";
    homepage    = https://github.com/rbarrois/factory_boy;
    license     = licenses.mit;
  };
}
