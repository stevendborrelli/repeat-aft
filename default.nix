# -*- mode: nix -*-
{
  pkgs ? import <nixpkgs> { }
}:

# To use: run `nix-shell` or `nix-shell --run "exec zsh"`
# https://nixos.org/wiki/Development_Environments
# http://nixos.org/nix/manual/#sec-nix-shell

let
  # Pin a nixpkgs version
  pinned_pkgs = import (pkgs.fetchFromGitHub {
    owner  = "NixOS";
    repo   = "nixpkgs";
    rev    = "17.03";
    sha256 = "1fw9ryrz1qzbaxnjqqf91yxk1pb9hgci0z0pzw53f675almmv9q2";
  }) {};

  jsonschema_c = pinned_pkgs.callPackage ./jsonschema-c.nix { };

in with pinned_pkgs; stdenv.mkDerivation {
  name = "repeat-aft";
  src = ./.;
  buildInputs = [
    python3
    python3Packages.sphinx
    python3Packages.jsonschema
  ];

  meta = with stdenv.lib; {
    homepage = https://github.com/ripeta/repeat-aft;
    description = "";
    maintainers = with maintainers; [ siddharthist ];
    platforms = platforms.linux;
  };
}
