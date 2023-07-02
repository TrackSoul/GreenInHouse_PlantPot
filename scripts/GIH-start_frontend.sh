#!/bin/bash
#Author: Oscar Valverde Escobar



path_home=/GreenInHouse
path_script="$path_home"/script
cd "$path_script"

./GIH-configure_static_ip.sh

./GIH-stop_process.sh './GIH-run_app_rpi.sh' './GIH-frontend-app-rpi.sh' 
#lanzamiento retrasado de app de raspberry
$(nohup ./GIH-run_app_rpi.sh >> ./script_log/app_rpi.out 2>> ./script_log/app_rpi.err < /dev/null &)