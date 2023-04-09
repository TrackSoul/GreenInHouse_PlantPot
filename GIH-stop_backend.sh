#!/bin/bash

for pid in $(ps -a | grep -E 'GIH' | grep -oE ^[\ ]*[0-9]+ | grep -oE [0-9]+)
do
    if [ $(ps $(($pid)) | grep -E './GIH-stop_backend.sh' | wc -l) -ne 1 ]; then
        if [ $# -ge 1 ]; then
            if [ $(ps $(($pid)) | grep -E $1 | wc -l) -ne 1 ]; then
                $(kill $(($pid)) 2> /dev/null)
            fi
        else
            $(kill $(($pid)) 2> /dev/null)
        fi
    fi
done


