{ lib, buildPythonPackage, fetchPypi, pyyaml }:

buildPythonPackage rec {
  pname = "aspy.yaml";
  version = "0.3.0";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "129wdxgkxw2h8asa2mw0l6vagvmvh60ya96sy88y5pa9b5nd90py";
  };

  propagatedBuildInputs = [ pyyaml ];

  meta = {
    homepage = "https://github.com/asottile/aspy.yaml";
    description = "Some extensions to pyyaml";
    license = lib.licenses.mit;
  };
}
