{ stdenv, lib, fetchzip }:

stdenv.mkDerivation {
  name = "nltk_data.punkt";
  src = fetchzip {
    url = https://github.com/nltk/nltk_data/raw/gh-pages/packages/tokenizers/punkt.zip;
    sha256 = "11xckn0jfdqcqdpmmslj4b1hpfhyxn59yadx2xsbka3kkb60mx61";
  };

  installPhase = ''
    mkdir -p $out/tokenizers/punkt/PY3/
    cp -r . $out/tokenizers/punkt/PY3/
  '';
}
