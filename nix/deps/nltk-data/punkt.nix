{ stdenv, lib, fetchurl }:

stdenv.mkDerivation {
  name = "nltk_data.punkt";

  src = fetchurl {
    url = https://github.com/ripeta/nltk_data/raw/fd2cbbc424f6b497bd5e2eeabef81b5d0d0613e4/packages/tokenizers/punkt.tar.gz;
    sha256 = "07h6c4rlk6cz45z2n3gy7frvjsl8vzyn008kh0cc4av3ykrga3dp";

  };

  installPhase = ''
    mkdir -p $out/tokenizers/punkt/PY3/
    cp -r . $out/tokenizers/punkt/PY3/
  '';
}
