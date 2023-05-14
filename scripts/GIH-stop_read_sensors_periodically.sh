#!/bin/bash

path_home=/GreenInHouse
path_script="$path_home"/script
cd "$path_script"

./GIH-stop_process.sh './GIH-run_read_sensors_periodically.sh' './GIH-backend-read-sensors'

