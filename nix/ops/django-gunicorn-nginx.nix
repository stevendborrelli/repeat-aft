{
  app,                 # Django app, packaged with buildPythonPackage
  bash,                #
  python3,             # TODO: remove
  nginx,               #
  gunicorn,            #
  externalPort ? 80,   # nginx will listen for connections here
  internalPort ? 8000  # gunicorn will listen for connections here
}:

let
  # gunicorn has to have access to all the modules that our app requires
  guni = gunicorn.overrideAttrs (oldAttrs: {
    propagatedBuildInputs =
      oldAttrs.propagatedBuildInputs ++ app.propagatedBuildInputs ++ [ app ];
  });
in {
  environment.systemPackages = [ python3 guni ];
  users.extraUsers = { django = { }; };
  # TODO
  # networking.firewall.allowedTCPPorts = [ 80 ];
  networking.firewall.enable = false;

  # nginx just passes off connections to gunicorn
  services = {
    nginx = {
      enable = true;
      httpConfig = ''
        server {
          listen ${toString externalPort} default_server;
          server_name _;
          location /static/ {
              alias ${app}/lib/python3.6/site-packages/${app.pname}/static/;
          }
          location / {
            proxy_pass http://localhost:${toString internalPort};
          }
        }
      '';
    };

    openssh.enable = true;
  };

  systemd.services = {
    repeat = {
      enable = true;
      description = "${app.pname}";
      wants = [ "nginx.service" ];
      after = [ "network.target" ];
      serviceConfig = {
          ExecStartPre = ''\
            ${bash}/bin/bash -c \
              '${app}/bin/manage.py makemigrations; \
               ${app}/bin/manage.py migrate --run-syncdb'
          '';
          ExecStart = ''\
            ${guni}/bin/gunicorn \
              --bind 'localhost:${toString internalPort}' \
              '${app.pname}.wsgi'
          '';
          Restart = "always";
          User = "django";
      };
    };
  };
}
