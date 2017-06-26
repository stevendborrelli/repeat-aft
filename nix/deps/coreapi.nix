{ lib, buildPythonPackage, fetchPypi,
  # Library dependencies
  coreschema, itypes, requests, uritemplate }:

buildPythonPackage rec {
  pname = "coreapi";
  version = "2.3.1";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "054p4hhk0ig4xcbffkgj9hf4ylq5yry7zg9kxzlhsh8mfjnvb25g";
  };

  propagatedBuildInputs = [ coreschema itypes requests uritemplate ];

  meta = {
    homepage = "";
    description = "";
    license = lib.licenses.bsd3;
  };
}
