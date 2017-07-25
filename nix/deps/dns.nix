{ buildPythonPackage, fetchzip, lib }:

buildPythonPackage rec {
  pname = "dnspython";
  version = "1.15.0";
  name = "${pname}-${version}";

  src = fetchzip {
    url = "https://files.pythonhosted.org/packages/e4/96/a598fa35f8a625bc39fed50cdbe3fd8a52ef215ef8475c17cabade6656cb/dnspython-1.15.0.zip";
    sha256 = "0fx2v8g13y64s8aaw1qxj5jk5zilbcdb2mrzsaf13qav3lncf8i2";
  };

  # needs networking for some tests
  doCheck = false;

  meta = {
    description = "A DNS toolkit for Python 3.x";
    homepage = http://www.dnspython.org;
    # BSD-like, check http://www.dnspython.org/LICENSE for details
    license = lib.licenses.free;
  };
}
