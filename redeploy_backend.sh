#!/bin/bash

original_path=$(pwd)
path_intall=~/GrenInHouse

yes | cp -arf "$original_path"/. "$path_intall"

source "$path_intall"/venv_backend/.venv/bin/activate


cd "$path_intall"/components/common
./install.sh

cd "$path_intall"/components/backend
./install.sh
./start.sh