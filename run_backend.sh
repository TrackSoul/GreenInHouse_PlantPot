#!/bin/bash

path_install=~/GreenInHouse
source "$path_install"/venv_backend/.venv/bin/activate

cd "$path_install"/components/backend
./start.sh