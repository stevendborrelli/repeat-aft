Nix
===

This project uses `Nix <http://nixos.org/nix/>`_ to manage its dependencies. We
use some packages that have not made it into a stable version of the Nix package
set (`NixOS/nixpkgs <https://github.com/NixOS/nixpkgs/>`_. These packages are
under ``nix/deps/``.

We could point Nix to an update package set (rather than maintain these ``.nix``
files in this repo), but that would cause us to lose the benefits of the
`Nix binary cache <https://nixos.org/nix/manual/#ch-basic-package-mgmt>`_.
