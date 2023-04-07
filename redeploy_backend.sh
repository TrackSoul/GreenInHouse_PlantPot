#!/bin/bash
original_path=$(pwd)
path_install=~/GreenInHouse
yes | cp -arf "$original_path"/. "$path_install"
./deploy_backend.sh