#!/bin/bash
#ejecutar con sudo

./GIH-stop_except.sh './GIH-deploy' './GIH-reinstall' './GIH-install'

cd ..
original_path=$(pwd)
path_home=/GreenInHouse
path_script="$path_home"/script
path_db="$path_home"/db
path_venv="$path_home"/venv
path_cfg="$path_home"/cfg

rm -rfd "$path_script"
cp -af "$original_path"/scripts "$path_script"
if [ ! -d "$path_script"/script_log ]; then
    mkdir "$path_script"/script_log
fi
chmod -R 777 "$path_script"

rm -rfd "$path_cfg"
cp -af "$original_path"/config "$path_cfg"
chmod -R 777 "$path_cfg"

source "$path_venv"/venv_frontend/venv_frontend_app_rpi/.venv/bin/activate
cd "$original_path"/components/common
./GIH-install.sh
cd "$original_path"/components/frontend
./GIH-install.sh

line='@reboot /GreenInHouse/script/GIH-start_backend.sh'
for usuario in $(who | cut -d ' ' -f 1)
do
    if [ $(crontab -u "$usuario" -l | grep -e "$line" | wc -l) -eq 0 ]; then
        (crontab -u "$usuario" -l; echo "$line" ) | crontab -u "$usuario" -
    fi
done

cp -f "$original_path"/init/GreenInHouse.desktop /etc/xdg/autostart