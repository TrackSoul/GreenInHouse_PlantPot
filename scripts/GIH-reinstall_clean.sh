#!/bin/bash
#Author: Oscar Valverde Escobar

#ejecutar con sudo

./GIH-stop_except.sh './GIH-reinstall' './GIH-install'

./GIH-reinstall_clean_backend.sh
./GIH-reinstall_frontend.sh

#configuracion de direccion IP
./GIH-configure_static_ip.sh