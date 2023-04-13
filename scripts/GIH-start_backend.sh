#!/bin/bash

if [ $# -lt 1 ]; then 
    sleep_time=600
else
    sleep_time=$1
fi

./GIH-stop_backend.sh './GIH-start_backend.sh'

path_home=/GreenInHouse
path_venv="$path_home"/venv
path_script="$path_home"/script

cd "$path_script"

#lectura periodica de sensores
$(nohup ./GIH-run_periodic_read_sensors.sh $sleep_time >> ./script_log/periodic_read_sensors.out 2>> ./script_log/periodic_read_sensors.err < /dev/null &)
#lanzamiento de api rest
$(nohup ./GIH-run_api_rest.sh >> ./script_log/api_rest.out 2>> ./script_log/api_rest.err < /dev/null &)
