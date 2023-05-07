import tkinter as tk
from tkinter import ttk
def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.config(width=300, height=200)
    # Crear un botón dentro de la ventana secundaria
    # para cerrar la misma.
    boton_cerrar = ttk.Button(
        ventana_secundaria,
        text="Cerrar ventana", 
        command=ventana_secundaria.destroy
    )
    boton_cerrar.place(x=75, y=75)
    ventana_secundaria.focus()
    ventana_secundaria.grab_set()
# Crear la ventana principal.
ventana_principal = tk.Tk()
ventana_principal.config(width=400, height=300)
ventana_principal.title("Ventana principal")
# Crear un botón dentro de la ventana principal
# que al ejecutarse invoca a la función
# abrir_ventana_secundaria().
boton_abrir = ttk.Button(
    ventana_principal,
    text="Abrir ventana secundaria",
    command=abrir_ventana_secundaria
)
boton_abrir.place(x=100, y=100)
ventana_principal.mainloop()