#!/bin/bash
#ejecutar con sudo

path_db=/GreenInHouse/db
rm -f "$path_db"/GreenInHouseBackend.sqlite3.db
./GIH-reinstall_backend.sh


