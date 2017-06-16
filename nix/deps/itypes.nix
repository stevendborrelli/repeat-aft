{ lib, buildPythonPackage, fetchPypi }:

buildPythonPackage rec {
  pname = "itypes";
  version = "1.1.0";
  name = "${pname}-${version}";

  src = fetchPypi {
    inherit pname version;
    sha256 = "0wy0k6l85nwlxh9lkb2vl98j8a02311fm3wmkpmvz938znwppry6";
  };

  meta = {
    homepage = "";
    description = "";
    license = lib.licenses.bsd3;
  };
}
