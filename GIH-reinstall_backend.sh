#!/bin/bash
#ejecutar con sudo

./GIH-stop_backend.sh './GIH-reinstall'

path_install=/GreenInHouse/src
rm -rfd "$path_install"
./GIH-install_backend.sh
