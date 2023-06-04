import tkinter as tk
from tkinter import ttk
from frontend.app.rpi import VentanaTeclado
from common.service import WifiService
import tkinter.font as font

class VentanaConfigurarWifi(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.callback = callback
        self.config(width=800, height=440)

        # self.resizable(0, 0)

        self.title("Configuracion de red WiFi")

        self.ssid = tk.StringVar()
        self.caja_ssid = ttk.Entry(self,  textvariable=self.ssid, font=('Arial', 20))
        self.caja_ssid.place(x=420, y=100, width=300)     
        self.boton_introducir_ssid = ttk.Button(
            self,
            text="Nombre WiFi:",
            command=self.introducir_ssid
        )
        self.boton_introducir_ssid.place(x=80, y=100, width=300)

        self.psk = tk.StringVar()
        self.caja_psk = ttk.Entry(self, textvariable=self.psk, font=('Arial', 20))
        self.caja_psk.place(x=420, y=200, width=300)   
        self.boton_introducir_psk = ttk.Button(
            self,
            text="Contraseña WiFi:",
            command=self.introducir_psk
        )
        self.boton_introducir_psk.place(x=80, y=200, width=300)

        self.boton_cancelar = ttk.Button(
            self,
            text="Cancelar",
            command=self.cancelar
        )
        self.boton_cancelar.place(x=60, y=300, width=300)

        self.boton_aceptar = ttk.Button(
            self,
            text="Aceptar",
            command=self.aceptar
        )
        self.boton_aceptar.place(x=440, y=300, width=300)
        self.focus()
        self.grab_set()

    def introducir_ssid(self):
        self.ventana_ssid = VentanaTeclado(
            callback=self.ssid.set
        )

    def introducir_psk(self):
        self.ventana_psk = VentanaTeclado(
            callback=self.psk.set
        )
    
    def aceptar(self):
        WifiService.connect_wifi(self.caja_ssid.get(),self.caja_psk.get())
        self.callback("Necesario reiniciar para aplicar cambios")
        self.destroy()

    def cancelar(self):
        self.destroy()
