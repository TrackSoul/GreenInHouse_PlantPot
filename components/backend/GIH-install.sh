#!/bin/bash
#Author: Jesús Alonso Abad
#Author: Oscar Valverde Escobar

TEMP_DIR="$(mktemp -d)"

# Install
cp -R * "${TEMP_DIR}"
pushd "${TEMP_DIR}"
pip3 install .
popd

rm -R "${TEMP_DIR}"
