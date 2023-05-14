#!/bin/bash
#ejecutar con sudo

./GIH-stop_except.sh './GIH-reinstall' './GIH-install'

#path_install=/GreenInHouse/src
path_script=/GreenInHouse/script
path_venv=/GreenInHouse/venv

#rm -rfd "$path_install"
rm -rfd "$path_script"
rm -rfd "$path_venv"/venv_backend

./GIH-install_backend.sh
