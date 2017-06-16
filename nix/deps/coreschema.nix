{ lib, buildPythonPackage, fetchPypi, jinja2 }:

buildPythonPackage rec {
  pname = "coreschema";
  version = "0.0.4";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "01qn9bfkklpjkr0zn6bd5fr372n1jd5p455scw4ap0nl0xh500wm";
  };

  propagatedBuildInputs = [ jinja2 ];

  doCheck = false;

  meta = {
    homepage = "";
    description = "";
    license = lib.licenses.bsd3;
  };
}
