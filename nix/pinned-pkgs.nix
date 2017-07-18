{ pkgs ? import <nixpkgs> { } }:

# We need a version more recent than 17.03 for a newer version of django-rest-framework, faker, and factory_boy
import (pkgs.fetchFromGitHub {
  # TODO: See NixOS/nixpkgs#27106 and ripeta/repeat-aft#19
  owner  = "siddharthist";
  repo   = "nixpkgs";
  rev    = "f4c4a74624e116c0ba1e606eaacd7407f322d340";
  sha256 = "1mg5fwfm2690ci7yhx7b84gqm2gynkfm8s13ipglsnbzqvxqd54p";
}) { }
