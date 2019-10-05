#!/bin/bash

# Print script commands.
set -x
# Exit on errors.
set -e

# BMv2 related
git clone https://github.com/p4lang/behavioral-model.git bmv2
git clone https://github.com/p4lang/p4c-bm.git p4c-bmv2
cd p4c-bmv2
sudo pip install -r requirements.txt
cd ..

cd bmv2
./install_deps.sh
./autogen.sh
./configure
make

# Mininet
sudo apt-get --yes install mininet
sudo pip install scapy thrift networkx
