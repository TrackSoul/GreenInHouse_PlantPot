#!/bin/bash
#Author: Oscar Valverde Escobar

#Los siguientes comandos sirven actualizar el sistema operativo a la última versión:
sudo apt-get update && sudo apt-get install -f
sudo apt-get dist-upgrade

#Ejecución del siguiente comando para realizar la actualización de las headers del sistema y de lo módulos necesarios:
sudo apt install -y linux-headers raspberrypi-kernel-headers build-essential bc dkms git

#Reiniciar el sistema.

#Clonado del repositorio donde está almacenado su driver (para ello realicé un fork de la versión de los drivers que funcionaron en mi sistema, ya que probé muchos hasta encontrar unos que funcionasen correctamente):
git clone https://github.com/ove1001/88x2bu-20210702

#Ejecutar el script de instalación alojado en el interior del repositorio descargado:
cd 88x2bu-20210702
sudo ./install-driver.sh

#Reiniciar el sistema.

#Comprobar que el adaptador WiFi USB se reconoce correctamente:
lsusb

#Editar el fichero de sistema que almacena las interfaces Ethernet:
sudo nano /etc/network/interfaces
#Añadir en dicho fichero las siguientes lineas:
allow-hotplug wlan0
iface wlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

#Reiniciar el sistema.

#Tras este proceso el adaptador WiFi estará instalado y configurado para poder conectarse a una red WiFi mediante una dirección IP estática. Debido a algún tipo de bug en la interfaz gráfica, es posible que no se muestren las redes WiFi de alrededor, pero el adaptador WiFi funcionará correctamente. Para introducir las credenciales de la red WiFi se utilizará la App desarrollada en la pantalla táctil