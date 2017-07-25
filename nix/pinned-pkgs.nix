{ pkgs ? import <nixpkgs> { } }:

# This is the most recent nixpkgs 17.03 stable commit
import (pkgs.fetchFromGitHub {
  owner  = "NixOS";
  # repo   = "nixpkgs";
  # rev    = "17.03";
  # sha256 = "1fw9ryrz1qzbaxnjqqf91yxk1pb9hgci0z0pzw53f675almmv9q2";
  repo   = "nixpkgs-channels";
  rev    = "8d9c8383f921e84eac21d1125cbaee1f3fa97aed";
  sha256 = "04g1nx1rw32ryi8ghdbiyf2g08v3vimbrvki2mjyg33q6kpx6qig";
}) { }
