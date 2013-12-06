# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "base"
  config.vm.url = "http://files.vagrantup.com/precise32.box"
  config.vm.network :private_network, ip: "192.168.33.60"
  config.vm.provision :shell, :path => "bootstrap.sh"
end
