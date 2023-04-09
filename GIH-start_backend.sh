#!/bin/bash

if [ $# -lt 1 ]; then 
    sleep_time=600
else
    sleep_time=$1
fi

for pid in $(ps -a | grep -E 'GIH' | grep -oE ^[\ ]*[0-9]+ | grep -oE [0-9]+)
do
    if [ $(ps $(($pid)) | grep -E './GIH-start_backend.sh' | wc -l) -ne 1 ]; then
        $(kill $(($pid)) 2> /dev/null)
    fi
done

#lectura periodica de sensores
$(nohup ./GIH-run_periodic_read_sensors.sh $sleep_time > script_log/periodic_read_sensors.out 2> script_log/periodic_read_sensors.err < /dev/null &)
#lanzamiento de api rest
$(nohup ./GIH-run_api_rest.sh > script_log/api_rest.out 2> script_log/api_rest.err < /dev/null &)
