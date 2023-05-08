#!/bin/bash

./GIH-stop.sh './GIH-deploy' './GIH-reinstall' './GIH-install'

path_db=/GreenInHouse/db
rm -f "$path_db"/GreenInHouseBackend.sqlite3.db
./GIH-deploy_backend.sh
