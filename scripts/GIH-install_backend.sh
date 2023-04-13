#!/bin/bash
#ejecutar con sudo

./GIH-stop_backend.sh './GIH-install'

apt-get update
apt-get upgrade
apt-get install python3-dev python3-pip
apt install python3.8-venv
apt install sqlite3
apt-get install nmap

original_path=$(pwd)
path_home=/GreenInHouse
path_script="$path_home"/script
path_db="$path_home"/db
path_venv="$path_home"/venv

mkdir -p "$path_home"
mkdir -p "$path_script"
mkdir -p "$path_db"
mkdir -p "$path_venv"
if [ ! -d "$path_script"/script_log ]; then
    mkdir "$path_script"/script_log
fi

cd "$path_venv"

#venv api rest - bd
mkdir -p venv_backend
cd "$path_venv"/venv_backend
mkdir -p venv_backend_api_rest
cd "$path_venv"/venv_backend/venv_backend_api_rest
python3 -m venv .venv
source "$path_venv"/venv_backend/venv_backend_api_rest/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install flask connexion sqlalchemy==2.0.0b3 pyyaml
pip3 install connexion[swagger-ui]
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx

#venv sensors - db
cd "$path_venv"/venv_backend
mkdir -p venv_backend_sensors
cd "$path_venv"/venv_backend/venv_backend_sensors
python3 -m venv .venv
source "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install sqlalchemy==2.0.0b3 pyyaml
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx

cd "$original_path"
./GIH-deploy_backend.sh

