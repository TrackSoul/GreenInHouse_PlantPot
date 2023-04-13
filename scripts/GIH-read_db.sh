#!/bin/bash

#path_install=/GreenInHouse/src
path_venv=/GreenInHouse/venv

source "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin/activate

#cd "$path_install"/components/backend
#./GIH-start-read-db.sh

cd "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin
./GIH-backend-read-db