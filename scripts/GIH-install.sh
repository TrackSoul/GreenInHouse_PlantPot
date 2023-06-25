#!/bin/bash
#Author: Oscar Valverde Escobar

#ejecutar con sudo

./GIH-stop_except.sh './GIH-reinstall' './GIH-install'

apt-get update
apt-get upgrade
apt-get install python3-dev python3-pip python3-wheel
apt install python3.9-venv
apt install sqlite3
apt-get install nmap
apt install network-manager

#change permisions of wpa_spplicant.conf to permit update network form app
sudo chmod 666 /etc/wpa_supplicant/wpa_supplicant.conf

original_path=$(pwd)
path_home=/GreenInHouse
path_script="$path_home"/script
path_db="$path_home"/db
path_venv="$path_home"/venv

mkdir -p "$path_home"
mkdir -p "$path_script"
mkdir -p "$path_db"
mkdir -p "$path_venv"
if [ ! -d "$path_script"/script_log ]; then
    mkdir "$path_script"/script_log
fi

cd "$original_path"
./GIH-install_backend.sh
./GIH-install_frontend.sh
./GIH-configure_static_ip.sh 

reboot now