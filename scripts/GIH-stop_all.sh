#!/bin/bash
#Author: Oscar Valverde Escobar


for pid in $(ps -ax | grep -E 'GIH' | grep -oE ^[\ ]*[0-9]+ | grep -oE [0-9]+)
do
    if [ $(ps $(($pid)) | grep -E './GIH-stop_all.sh' | wc -l) -ne 1 ]; then
        $(kill $(($pid)) 2> /dev/null)
    fi
done


