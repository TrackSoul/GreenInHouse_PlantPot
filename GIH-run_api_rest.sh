#!/bin/bash

path_install=/GreenInHouse/src
source "$path_install"/venv_backend/venv_backend_api_rest/.venv/bin/activate

cd "$path_install"/components/backend
./GIH-start-api-rest.sh