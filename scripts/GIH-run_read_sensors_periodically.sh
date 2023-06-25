#!/bin/bash
#Author: Oscar Valverde Escobar


if [ $# -lt 1 ]; then 
    sleep_time=600
else
    sleep_time=$1
fi

path_venv=/GreenInHouse/venv
cd "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin
source ./activate

while :
do
    ./GIH-backend-read-sensors &
	sleep $sleep_time
done
