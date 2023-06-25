#Author: Oscar Valverde Escobar

import tkinter as tk
from tkinter import ttk
from frontend.app.rpi import VentanaConfigurarWifi
from common.service import WifiService
import os

class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=800, height=440)
        # self.geometry('800x440')  # Window size
        # self.maxsize(width=800, height=440)
        # self.minsize(width=800, height=440)
        self.title("Green In House")

        self.configure(bg='gray99')
        # self.configure(font=('Arial', 20))

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 20))
        self.style.configure('TButton', background='azure')
        self.style.configure('TButton', foreground='black')

        self.style.configure('TEntry', font=('Arial', 20))

        self.style.configure('TLabel', font=('Arial', 20))

        wifi_conected=WifiService().wifi_conected()
        if len(wifi_conected[0])==0:
            self.etiqueta_wifi_conectado = ttk.Label(
                self,
                text="Sin conexion a red WiFi"
            )
        else:
            self.etiqueta_wifi_conectado = ttk.Label(
                self,
                text="Conectado a red WiFi: " + wifi_conected[1]
            )
        self.etiqueta_wifi_conectado.place(x=200, y=20)

        self.boton_configurar_wifi = ttk.Button(
            self,
            text="Conectarse a red WiFi",
            command=self.conectarse_a_red_wifi
        )
        self.boton_configurar_wifi.place(x=300, y=80)

        self.boton_reiniciar = ttk.Button(
            self,
            text="Reiniciar",
            command=self.reiniciar
        )
        self.boton_reiniciar.place(x=60, y=300, width=300)

        self.boton_apagar = ttk.Button(
            self,
            text="Apagar",
            command=self.apagar
        )
        self.boton_apagar.place(x=440, y=300, width=300)
        
    def conectarse_a_red_wifi(self):
        self.ventana_nombre = VentanaConfigurarWifi(
            callback=self.wifi_conectado
        )
    
    def wifi_conectado(self, respuesta):
        self.etiqueta_wifi_conectado.config(
            text=respuesta
        )

    def reiniciar(self):
        command = "shutdown -r now"
        os.popen((command.format()))

    def apagar(self):
        command = "shutdown now"
        os.popen((command.format()))

# if __name__ == '__main__':        
#     ventana_principal = VentanaPrincipal()
#     ventana_principal.mainloop()