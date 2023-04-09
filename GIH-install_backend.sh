#!/bin/bash
#ejecutar con sudo

apt-get update
apt-get upgrade
apt-get install python3-dev python3-pip
apt install python3.8-venv
apt install sqlite3
apt-get install nmap

original_path=$(pwd)
path_home=/GreenInHouse
path_install=/GreenInHouse/src
path_db=/GreenInHouse/db

mkdir -p "$path_home"
mkdir -p "$path_install"
mkdir -p "$path_db"

#cp -a "$original_path"/. "$path_install"
cd "$path_install"

#venv api rest - bd
mkdir -p venv_backend
cd "$path_install"/venv_backend
mkdir -p venv_backend_api_rest
cd "$path_install"/venv_backend/venv_backend_api_rest
python3 -m venv .venv
source "$path_install"/venv_backend/venv_backend_api_rest/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install flask connexion sqlalchemy==2.0.0b3 pyyaml
pip3 install connexion[swagger-ui]
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx

cd "$original_path"/components/common
./GIH-install.sh
cd "$original_path"/components/backend
./GIH-install.sh

#venv sensors - db
cd "$path_install"/venv_backend
mkdir -p venv_backend_sensors
cd "$path_install"/venv_backend/venv_backend_sensors
python3 -m venv .venv
source "$path_install"/venv_backend/venv_backend_sensors/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install sqlalchemy==2.0.0b3 pyyaml
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx

cd "$original_path"/components/common
./GIH-install.sh
cd "$original_path"/components/backend
./GIH-install.sh

cd "$original_path"
./GIH-deploy_backend.sh

chmod -R 777 "$path_home"