#!/bin/bash
#ejecutar con sudo

./GIH-stop_except.sh './GIH-reinstall' './GIH-install'

./GIH-reinstall_clean_backend.sh
./GIH-reinstall_frontend.sh