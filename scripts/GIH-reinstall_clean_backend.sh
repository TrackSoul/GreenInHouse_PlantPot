#!/bin/bash
#ejecutar con sudo

./GIH-stop.sh './GIH-reinstall' './GIH-install'

path_db=/GreenInHouse/db
rm -f "$path_db"/GreenInHouseBackend.sqlite3.db

./GIH-reinstall_backend.sh


