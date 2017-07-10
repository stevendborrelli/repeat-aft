{ pkgs ? import <nixpkgs> { } }:

# We need a version more recent than 17.03 for a newer version of django-rest-framework, faker, and factory_boy
import (pkgs.fetchFromGitHub {
  # TODO: See NixOS/nixpkgs#27106 and ripeta/repeat-aft#19
  owner  = "siddharthist";
  repo   = "nixpkgs";
  rev    = "41a598fedab06a5d0dbc05ca3bb997fd649fa4f5";
  sha256 = "1d2c4wqhh68sbqabbcjf08ivbzk8pg037b7wsckd6v1xcgd3ik72";
}) { }
