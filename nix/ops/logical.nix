{
  network.description = "Django web server";

  webserver =
    { config, pkgs, lib, ... }:
    let
      pinnedPkgs = import ../pinned-pkgs.nix { pkgs = pkgs; };
    in with pinnedPkgs;

    import ./django-gunicorn-nginx.nix rec {
      inherit bash nginx;
      app = callPackage ../../default.nix { pkgs = pinnedPkgs; };
      python3 = python36;
      gunicorn = python36Packages.gunicorn;
      environment = { NLTK_DATA = app.NLTK_DATA; };
    };
}
