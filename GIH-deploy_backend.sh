#!/bin/bash

./GIH-stop_backend.sh './GIH-deploy'

original_path=$(pwd)
path_home=/GreenInHouse
path_install=/GreenInHouse/src
path_db=/GreenInHouse/db

yes | cp -arf "$original_path"/. "$path_install"

if [ $(sqlite3 "$path_db"/GreenInHouseBackend.sqlite3.db .dump | grep -iE 'insert'| wc -l) -lt 1 ]; then
    source "$path_install"/venv_backend/venv_backend_sensors/.venv/bin/activate
    cd "$path_install"/components/backend
    ./GIH-initialize.sh
fi
