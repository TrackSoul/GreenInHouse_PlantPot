#!/bin/bash
#ejecutar con sudo

./GIH-stop_except.sh './GIH-reinstall' './GIH-install'

original_path=$(pwd)
path_home=/GreenInHouse
path_script="$path_home"/script
path_db="$path_home"/db
path_venv="$path_home"/venv

cd "$path_venv"
#venv api rest - bd
mkdir -p venv_backend
cd "$path_venv"/venv_backend
mkdir -p venv_backend_api_rest
cd "$path_venv"/venv_backend/venv_backend_api_rest
python3 -m venv .venv
source "$path_venv"/venv_backend/venv_backend_api_rest/.venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install flask connexion==2.14.2 sqlalchemy==2.0.0b3 pyyaml
pip3 install connexion[swagger-ui]
pip3 install gpiod
pip3 install adafruit-circuitpython-dht
pip3 install adafruit-circuitpython-mcp3xxx
pip3 install arrow

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
pip3 install arrow

cd "$original_path"
./GIH-deploy_backend.sh

line='@reboot /GreenInHouse/script/GIH-start_all.sh'
for usuario in $(who | cut -d ' ' -f 1)
do
    if [ $(crontab -u "$usuario" -l | grep -e "$line" | wc -l) -eq 0 ]; then
        (crontab -u "$usuario" -l; echo "$line" ) | crontab -u "$usuario" -
    fi
done