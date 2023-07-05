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
chmod 666 /etc/wpa_supplicant/wpa_supplicant.conf

#Habilitación de puertos de comunicacion
raspi-config nonint do_ssh 0
raspi-config nonint do_vnc 0
raspi-config nonint do_i2c 0
raspi-config nonint do_spi 0
raspi-config nonint do_serial 0
raspi-config nonint do_onewire 0
raspi-config nonint do_rgpio 0
#cambio nombre de hostname
raspi-config nonint do_hostname GreenInHouse

./GIH-reinstall_backend.sh
./GIH-reinstall_frontend.sh

#configuracion de direccion IP
./GIH-configure_static_ip.sh

reboot now