#!/bin/bash

if [ $# -lt 1 ]; then 
    sleep_time=600
else
    sleep_time=$1
fi

path_install=/GreenInHouse/src
path_venv=/GreenInHouse/venv

source "$path_venv"/venv_backend/venv_backend_sensors/.venv/bin/activate

cd "$path_install"/components/backend

while :
do
	./GIH-start-read-sensors.sh
	sleep $sleep_time
done
