# Web Security Proof of Concept

You can find my first talk on XSS and SQL injection on https://speakerdeck.com/yeukhon/introduction-to-web-security

## Getting Started


- VirtualBox (https://www.virtualbox.org/wiki/Downloads/)
- Vagrant (<http://docs.vagrantup.com/v2/>)
- PuTTY (http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) or another SSH client (Windows users only)


PuTTY users may need to follow the directions on `Stack Overflow` (http://stackoverflow.com/a/9924122/978961)

## Setup using a VM

After installing VirtualBox and Vagrant, clone the repository and start up the
virtual machine.

```
   $ git clone https://github.com/yeukhon/websec-poc.git
   $ cd websec-poc
   $ vagrant up --provision
```

The ``--provision`` is used to bootstrap the VM once the VM has been
created. Note if this is your first time the last command will take a 
while to complete because vagrant will download a ISO around 300MB.

```
   $ vagrant ssh
```

This command is only usable if you are under websec-poc. You can also
do ``ssh vagrant:vagrant@192.168.33.60``. This is the IP of the machine, by the
way.

When you are done, just ``vagrant halt``. And next time when you want to launch it
again, you just need to call ``vagrant up``.

## Setup locally

```
    $ git clone https://github.com/yeukhon/websec-poc.git
    $ cd websec-poc
    $ [sudo] ./bootstrap.sh
```

Note this will install MySQL and a bunch of stuff to your OS
and only works on Linux. So, use the VM please...

## Launch server

You need two terminals. Log into the VM in both terminals:

```
    $ cd websec-poc
    $ python server.py
    $ python attacker.py
```

And you can visit server in the browser by visiting ``http://192.168.33.60:8080``.

Read the source code to find what urls are accessible.
