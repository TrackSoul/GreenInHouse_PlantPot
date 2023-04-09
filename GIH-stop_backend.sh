#!/bin/bash

for pid in $(ps -a | grep -E 'GIH' | grep -oE ^[\ ]*[0-9]+ | grep -oE [0-9]+)
do
    #echo $(ps $(($pid)))
    #echo $(ps $(($pid)) | grep -E './GIH-stop_backend.sh' | wc -l)
    if [ $(ps $(($pid)) | grep -E './GIH-stop_backend.sh' | wc -l) -ne 1 ]; then
        $(kill $(($pid)) 2> /dev/null)
    fi
done


