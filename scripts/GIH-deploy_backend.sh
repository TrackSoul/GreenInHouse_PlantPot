#!/bin/bash
#ejecutar con sudo

./GIH-stop_except.sh './GIH-deploy' './GIH-reinstall' './GIH-install'

cd ..
original_path=$(pwd)
path_home=/GreenInHouse
path_script="$path_home"/script
path_db="$path_home"/db
path_venv="$path_home"/venv
path_cfg="$path_home"/cfg
path_init=~/.config/upstart

rm -rfd "$path_script"
cp -af "$original_path"/scripts "$path_script"
if [ ! -d "$path_script"/script_log ]; then
    mkdir "$path_script"/script_log
fi
chmod -R 777 "$path_script"


rm -rf "$path_cfg"
cp -af "$original_path"/config/ "$path_cfg"
chmod -R 777 "$path_cfg"

source "$path_venv"/venv_backend/venv_backend_api_rest/.venv/bin/activate
cd "$original_path"/components/common
./GIH-install.sh
cd "$original_path"/components/backend
./GIH-install.sh

source "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin/activate
cd "$original_path"/components/common
./GIH-install.sh
cd "$original_path"/components/backend
./GIH-install.sh

if [ $(sqlite3 "$path_db"/GreenInHouseBackend.sqlite3.db .dump | grep -iE 'insert'| wc -l) -lt 1 ]  || [ ! -f "$path_db"/GreenInHouseBackend.sqlite3.db ]; then
    source "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin/activate
    cd "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin
    ./GIH-backend-create-initial
    chmod 777 -R "$path_db"
fi