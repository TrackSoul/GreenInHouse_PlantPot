#!/bin/bash

if [ $# -lt 1 ]; then 
    sleep_read_time=600
else
    sleep_read_time=$1
fi

path_home=/GreenInHouse
path_script="$path_home"/script
cd "$path_script"

./GIH-stop_process.sh './GIH-run_read_sensors_periodically.sh' './GIH-backend-read-sensors'
#lectura periodica de sensores
$(nohup ./GIH-run_read_sensors_periodically.sh $sleep_read_time >> ./script_log/periodic_read_sensors.out 2>> ./script_log/periodic_read_sensors.err < /dev/null &)

./GIH-stop_process.sh './GIH-run_api_rest.sh' './GIH-backend-api-rest'
#lanzamiento de api rest
$(nohup ./GIH-run_api_rest.sh >> ./script_log/api_rest.out 2>> ./script_log/api_rest.err < /dev/null &)
