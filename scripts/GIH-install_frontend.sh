#!/bin/bash
#ejecutar con sudo

./GIH-stop.sh './GIH-reinstall' './GIH-install'

original_path=$(pwd)
path_home=/GreenInHouse
path_script="$path_home"/script
path_db="$path_home"/db
path_venv="$path_home"/venv

cd "$path_venv"
#venv app rpi
mkdir -p venv_frontend
cd "$path_venv"/venv_frontend
mkdir -p venv_frontend_app_rpi
cd "$path_venv"/venv_frontend/venv_frontend_app_rpi
python3 -m venv .venv
source "$path_venv"/venv_frontend/venv_frontend_app_rpi/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install sqlalchemy==2.0.0b3 pyyaml
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx
pip3 install tk

cd "$original_path"
./GIH-deploy_frontend.sh
