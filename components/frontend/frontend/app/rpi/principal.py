import tkinter as tk
from tkinter import ttk
from secundaria import VentanaNombre

class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Ventana principal")
        self.boton_solicitar_nombre = ttk.Button(
            self,
            text="Solicitar nombre",
            command=self.solicitar_nombre
        )
        self.boton_solicitar_nombre.place(x=50, y=50)
        self.etiqueta_nombre = ttk.Label(
            self,
            text="Aún no has ingresado ningún nombre."
        )
        self.etiqueta_nombre.place(x=50, y=150)
    def solicitar_nombre(self):
        # Crear la ventana secundaria y pasar como argumento
        # la función en la cual queremos recibir el dato
        # ingresado.
        self.ventana_nombre = VentanaNombre(
            callback=self.nombre_ingresado
        )
    
    def nombre_ingresado(self, nombre):
        # Esta función es invocada cuando el usuario presiona el
        # botón "¡Listo!" de la ventana secundaria. El dato
        # ingresado estará en el argumento "nombre".
        self.etiqueta_nombre.config(
            text="Ingresaste el nombre: " + nombre
        )
ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()