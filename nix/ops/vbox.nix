let
  vbox = { mem, cpu }: {
    deployment.targetEnv = "virtualbox";
    deployment.virtualbox = {
      memorySize = mem; # megabytes
      vcpu = cpu; # number of cpus
      headless = true;
    };
  };
in
{
  webserver = vbox { mem = 1024; cpu = 2; };
}
