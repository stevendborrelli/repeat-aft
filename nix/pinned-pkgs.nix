{ pkgs ? import <nixpkgs> { } }:

# TODO: get faker in nixpkgs
# https://github.com/NixOS/nixpkgs/pull/27106
import ../../nixpkgs { }

# We need a version more recent than 17.03 for a newer version of django-rest-framework
# import (pkgs.fetchFromGitHub {
#   owner  = "NixOS";
#   repo   = "nixpkgs";
#   rev    = "6b999f3c42607342231b6fe119fcf0f934f40fd8";
#   sha256 = "00pp0ci70dipyabglw6slrmqj6f1dsqyyhwfjj62rardk1di2fdg";
# }) { }
