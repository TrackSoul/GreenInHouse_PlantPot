#!/bin/bash

# if [ $# -lt 1 ]; then 
#     sleep_read_time=600
# else
#     sleep_read_time=$1
# fi

# path_home=/GreenInHouse
# path_script="$path_home"/script
# cd "$path_script"

# ./GIH-stop_except.sh './GIH-start_all.sh' './GIH-restart_all.sh'

# #lectura periodica de sensores
# $(nohup ./GIH-run_read_sensors_periodically.sh $sleep_read_time >> ./script_log/periodic_read_sensors.out 2>> ./script_log/periodic_read_sensors.err < /dev/null &)
# #lanzamiento de api rest
# $(nohup ./GIH-run_api_rest.sh >> ./script_log/api_rest.out 2>> ./script_log/api_rest.err < /dev/null &)

# #lanzamiento retrasado de app de raspberry
# # sleep 120
# $(nohup ./GIH-run_app_rpi.sh >> ./script_log/app_rpi.out 2>> ./script_log/app_rpi.err < /dev/null &)

./GIH-start_backend.sh
./GIH-start_frontend.sh