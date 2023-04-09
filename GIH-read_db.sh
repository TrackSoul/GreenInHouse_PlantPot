#!/bin/bash

path_install=/GreenInHouse/src
source "$path_install"/venv_backend/venv_backend_sensors/.venv/bin/activate

cd "$path_install"/components/backend
./GIH-start-read-db.sh