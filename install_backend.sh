#!/bin/bash

apt-get update
apt-get upgrade
apt-get install python3-dev python3-pip

apt install python3.8-venv
apt install sqlite3

apt-get install nmap

original_path=$(pwd)

# cd "$original_path"/components/common
# chmod 777 install.sh
# cd "$original_path"/components/backend
# chmod 777 install.sh
# chmod 777 initialize.sh
# chmod 777 start.sh

path_install=~/GreenInHouse
mkdir -p "$path_install"
cp -a "$original_path"/. "$path_install"
cd "$path_install"
mkdir -p venv_backend
cd "$path_install"/venv_backend
python3 -m venv .venv
source "$path_install"/venv_backend/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install flask connexion sqlalchemy==2.0.0b3 pyyaml
pip3 install connexion[swagger-ui]
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx

cd "$original_path"
./deploy_backend.sh
