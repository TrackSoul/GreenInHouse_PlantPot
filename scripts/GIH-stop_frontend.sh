#!/bin/bash
#Author: Oscar Valverde Escobar



path_home=/GreenInHouse
path_script="$path_home"/script
cd "$path_script"

./GIH-stop_process.sh './GIH-run_app_rpi.sh' './GIH-frontend-app-rpi.sh' 
