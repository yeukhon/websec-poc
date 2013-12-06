#!/usr/bin/env bash

# Make sure everything is up to date
apt-get update

# Install the basics
apt-get install -y build-essential git vim mysql-server mysql-client python-virtualenv \
    python-dev python-mysqldb libmysqlclient-dev

pip install bottle mysql-python

echo "Do we need to clone websec-poc?"

if [ -d "/home/vagrant/websec-poc" ]; then
    # dude, it exists
    echo "Already cloned websec-poc"
else
    git clone https://github.com/yeukhon/websec-poc
fi

echo "What to do now? Fire up two terminals and do vagrant up and then fire up two servers!"
