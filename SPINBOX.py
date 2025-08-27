import tkinter as tk
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("Ejemplo de Spinbox")
ventana.geometry("300x200")
#spinbox de numeros del 1 al 10 para edad
def mostrarEdad():
    tk.messagebox.showinfo("Edad", f"La edad seleccionada es: {spin.get()}")
labelEdad=tk.Label(ventana, text="Edad")
labelEdad.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin= tk.Spinbox(ventana, from_=1, to=10)
spin.grid(row=0, column=1, padx=10, pady=10)
boton=tk.Button(ventana, text="Obetener valor", command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)
ventana.mainloop()