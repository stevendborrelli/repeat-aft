{ lib, buildPythonPackage, fetchPypi }:

buildPythonPackage rec {
  pname = "identify";
  version = "1.0.3";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "1xyrpk77kwn0yi6zdpvshyfls8lscppiwhkk2zd6p8vwj3b2gkxj";
  };

  meta = {
    homepage = "https://github.com/chriskuehl/identify";
    description = "File identification library for Python";
    license = lib.licenses.mit;
  };
}
