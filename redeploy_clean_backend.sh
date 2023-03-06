#!/bin/bash

original_path=$(pwd)
path_install=~/GreenInHouse

rm -f /tmp/GreenInHouseBackend.sqlite3.db

yes | cp -arf "$original_path"/. "$path_install"

source "$path_install"/venv_backend/.venv/bin/activate

cd "$path_install"/components/common
./install.sh

cd "$path_install"/components/backend
./install.sh
./initialize.sh
./start.sh