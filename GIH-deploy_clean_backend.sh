#!/bin/bash

./GIH-stop_backend.sh './GIH-deploy'

path_db=/GreenInHouse/db
rm -f "$path_db"/GreenInHouseBackend.sqlite3.db
./GIH-deploy_backend.sh
