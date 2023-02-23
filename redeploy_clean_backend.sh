#!/bin/bash

original_path=$(pwd)
path_install=~/GreenInHouse

rm -f /tmp/GreenInHouseBackend.sqlite3.db

yes | cp -arf "$original_path"/. "$s"

source "$s"/venv_backend/.venv/bin/activate

cd "$s"/components/common
./install.sh

cd "$s"/components/backend
./install.sh
./initialize.sh
./start.sh