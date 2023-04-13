#!/bin/bash

./GIH-stop_backend.sh './GIH-deploy'

original_path=$(pwd)
path_home=/GreenInHouse
path_install=/GreenInHouse/src
path_db=/GreenInHouse/db
path_venv=/GreenInHouse/venv

rm -rfd "$path_install"
cp -arf "$original_path"/. "$path_install"
chmod -R 777 "$path_install"

cd "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin
for script in $(ls | grep -E "GIH")
do
    rm -f $script
done
cp -arf "$original_path"/components/backend/bin/. ./
for script in $(ls | grep -E "GIH")
do
    chmod -R 777 $script
done

if [ $(sqlite3 "$path_db"/GreenInHouseBackend.sqlite3.db .dump | grep -iE 'insert'| wc -l) -lt 1 ]; then
    source "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin/activate
    cd "$original_path"/components/backend
    ./GIH-initialize.sh
    chmod 777 "$path_db"/GreenInHouseBackend.sqlite3.db
fi
