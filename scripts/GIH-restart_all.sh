#!/bin/bash

if [ $# -lt 1 ]; then 
    sleep_time=600
else
    sleep_time=$1
fi

path_home=/GreenInHouse
path_script="$path_home"/script
cd "$path_script"

./GIH-stop_except.sh './GIH-restart.sh'
./GIH-start.sh $sleep_time
