#!/bin/bash
path_install=~/GreenInHouse

source "$path_install"/venv_backend/.venv/bin/activate

cd "$path_install"/components/common
./install.sh

cd "$path_install"/components/backend
./install.sh
if [ ! -f /tmp/GreenInHouseBackend.sqlite3.db ]; then
    ./initialize.sh
fi