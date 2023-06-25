#!/bin/bash
#Author: Oscar Valverde Escobar

#ejecutar con sudo

./GIH-stop_process.sh './GIH-backend-api-rest' 

cd ..
original_path=$(pwd)
original_spec_path="$original_path"/components/backend/backend/openapi
path_home=/GreenInHouse
venv_spec_path="$path_home"/venv/venv_backend/venv_backend_api_rest/.venv/lib/python3.9/site-packages/backend
path_script="$path_home"/script

rm -rfd "$path_script"/script_log
rm -rfd "$venv_spec_path"/openapi
cp -af "$original_spec_path" "$venv_spec_path"
if [ ! -d "$path_script"/script_log ]; then
    mkdir "$path_script"/script_log
fi
chmod -R 777 "$path_script"
