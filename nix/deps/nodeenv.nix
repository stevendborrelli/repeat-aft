{ lib, buildPythonPackage, fetchPypi }:

buildPythonPackage rec {
  pname = "nodeenv";
  version = "1.1.4";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "0qzim0khzhrjv67m39j57nkzj90f663iqk0hazrmvcywjjkq6gqw";
  };

  propagatedBuildInputs = [ ];

  meta = {
    homepage = "https://github.com/ekalinin/nodeenv";
    description = "Virtual environment for Node.js & integrator with virtualenv";
    license = lib.licenses.bsd3;
  };
}
