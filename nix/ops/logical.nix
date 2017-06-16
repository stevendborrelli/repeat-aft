{
  network.description = "Django web server";

  webserver =
    { config, pkgs, lib, ... }:
    let
      pinned_pkgs = import ../pinned-pkgs.nix { pkgs = pkgs; };
      app = pinned_pkgs.callPackage ../../default.nix { pkgs = pinned_pkgs; };
    in
    {
      environment.systemPackages = [ pkgs.python3 ];
      systemd.services = {
        repeat = {
          enable = true;
          description = "repeat";
          after = [ "network.target" ];
          environment = { PYTHONUSERBASE = "${app}"; };
          serviceConfig = {
            ExecStartPre = "${pkgs.bash}/bin/bash -c '${app}/bin/manage.py makemigrations; ${app}/bin/manage.py migrate'";
            # TODO: not the debug server!
            ExecStart = "${pkgs.python3}/bin/python3 ${app}/bin/manage.py runserver";
            Restart = "always";
            User = "django";
          };
        };

        httpd = {
          enable = true;
          documentRoot = "/var/www"
        };
      }

      users.extraUsers = {
        # django = { hashedPassword = builtins.getEnv "VM_PASSWORD"; };
        django = { };
      };

      networking.firewall.allowedTCPPorts = [ 80 ];

      services.openssh.enable = true;
    };
}
