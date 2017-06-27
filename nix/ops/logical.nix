{
  network.description = "Django web server";

  webserver =
    { config, pkgs, lib, ... }:
    let
      pinnedPkgs = import ../pinned-pkgs.nix { pkgs = pkgs; };
    in with pinnedPkgs;

    import ./django-gunicorn-nginx.nix {
      app = callPackage ../../default.nix { pkgs = pinnedPkgs; };
      bash = bash;
      python3 = python36;
      gunicorn = python36Packages.gunicorn;
      nginx = nginx;
    };
}
