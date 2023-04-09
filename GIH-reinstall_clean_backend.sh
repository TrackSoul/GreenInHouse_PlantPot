#!/bin/bash
#ejecutar con sudo

./GIH-stop_backend.sh './GIH-reinstall'

path_db=/GreenInHouse/db
rm -f "$path_db"/GreenInHouseBackend.sqlite3.db
./GIH-reinstall_backend.sh


