#!/bin/bash
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

./GIH-reinstall_backend.sh
./GIH-reinstall_frontend.sh
./GIH-configure_static_ip.sh 

reboot now