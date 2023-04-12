#!/bin/bash
#ejecutar con sudo

./GIH-stop_backend.sh './GIH-reinstall'

path_install=/GreenInHouse/src
path_venv=/GreenInHouse/venv

rm -rfd "$path_install"
rm -rfd "$path_venv"

./GIH-install_backend.sh
