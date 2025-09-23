import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# -------------------------
# Interfaz gráfica

#FRAME DOCTORES
#LISTA DE PACIENTES (INICIALMENTE VACIA)
data=[]
#FUNCION PARA REGISTRAR PACIENTE
def registrar_datos():
    datos={  #Crear un diccionario con los datos registrados
        "Nombre": entry_nombre.get(),
        "Especialidad": combo_especialidad.get(),
        "Genero": genero.get(),
        "Años": años.get(),
        "Hospital": combo_hospital.get()
    }

#AGREGAR A LA LISTA
    data.append(datos)
    guardar_en_archivo()
    cargar_treeview()
#CARGAR EL TREEVIEW
def cargar_treeview():
#limpiar el treeview
   for datos in treeview.get_children():
       treeview.delete(datos)
#Insertar cada paciente
   for i, item in enumerate(data):
       treeview.insert(
           "", "end", iid=str(i),
           values=(
               item["Nombre"],
               item["Especialidad"],
               item["Genero"],
               item["Años"],
               item["Hospital"],
           )
       )
# -------------------------
#GUARDAR LOS REGISTROS EN UN ARCHIVO DE TEXTO PARA DOCTORES
def guardar_en_archivo():
    with open("doctoresRegistros.txt","w", encoding="utf-8") as Archivo:
        for datos in data:
            Archivo.write(
                f"{datos['Nombre']}|"
                f"{datos['Especialidad']}|"
                f"{datos['Genero']}|"
                f"{datos['Años']}|"
                f"{datos['Hospital']}\n"
            )
            
def cargar_desde_archivo():
    try:
        with open("doctoresRegistros.txt", "r", encoding="utf-8") as Archivo:
            data.clear()
            for linea in Archivo:
                registros=linea.strip().split("|")
                if len(registros)==5:
                    datos= {
                        "Nombre": registros[0],
                        "Especialidad": registros[1],
                        "Genero": registros[2],
                        "Años": registros[3],
                        "Hospital": registros[4],
                    }
                    data.append(datos)
        cargar_treeview()
    except FileNotFoundError:
        open("doctoresRegistros.txt", "w", encoding="utf-8").close()
        
#FUNCION ELIMINAR 
def eliminar_registro():
    seleccionado= treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Registro", f"¿Está seguro de eliminar el registro '{treeview.item(id_item, 'values')[0]}'?"):
            del data[indice]
            guardar_en_archivo() # GUARDAR LOS CAMBIOS EN EL ARCHIVO
            cargar_treeview()
            messagebox.showinfo("Eliminar Registro", "Registro eliminado exitosamente.")
        else: #este else es del if seleccionado
            messagebox.showwarning("Eliminar Registro", "No se ha seleccionado ningun registro")
#---------------------------
ventana = tk.Tk()
ventana.title("Registro de doctores")
ventana.geometry("800x520")
ventana.minsize(700, 450)

# Frame del formulario
form_frame = ttk.Frame(ventana, padding=(12, 10))
form_frame.grid(row=0, column=0, sticky="ew")
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=1)

# Nombre
lbl_nombre = ttk.Label(form_frame, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="w", padx=6, pady=6)
entry_nombre = ttk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, sticky="ew", padx=6, pady=6)

# Presentación
lbl_especialidad = ttk.Label(form_frame, text="Especialidad:")
lbl_especialidad.grid(row=1, column=0, sticky="w", padx=6, pady=6)
combo_especialidad = ttk.Combobox(form_frame, values=["Cardiologia", "Pediatria", "Traumatologia", "Ginecologia", "Oftalmologia"])
combo_especialidad.grid(row=1, column=1, sticky="ew", padx=6, pady=6)

#GENERO
labelGenero=tk.Label(form_frame, text="Genero: ")
labelGenero.grid(row=2, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #VALOR POR DEFECTO
radioMasculino=ttk.Radiobutton(form_frame, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=2, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(form_frame, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=1, sticky="w", padx=5)

#AÑOS DE SERVICIO
labelAños=tk.Label(form_frame, text="Años de Experiencia: ")
labelAños.grid(row=4, column=0, sticky="w", pady=5, padx=5)
valores=list(range(0, 30))
años=tk.Spinbox(form_frame, values=(valores))
años.grid(row=4, column=1, padx=10, pady=10, sticky="w")

#Hospital
lbl_hospital = ttk.Label(form_frame, text="Hospital:")
lbl_hospital.grid(row=5, column=0, sticky="w", padx=6, pady=6)
combo_hospital = ttk.Combobox(form_frame, values=["Caja Petrolera", "Caja Nacional", "Foianini", "Niño Jesus", "Las Americas"])
combo_hospital.grid(row=5, column=1, sticky="ew", padx=6, pady=6)

# Botones
btn_frame = ttk.Frame(form_frame)
btn_frame.grid(row=6, column=0, columnspan=2, sticky="ew", padx=6, pady=(10, 2))
btn_frame.columnconfigure((0, 1, 2, 3), weight=1)  # columnas equitativas

btn_registrar = ttk.Button(btn_frame, text="Registrar", command=registrar_datos)
btn_registrar.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

btn_eliminar = ttk.Button(btn_frame, text="Eliminar", command=eliminar_registro)
btn_eliminar.grid(row=6, column=1, padx=5, pady=5, sticky="ew")


# Frame lista
list_frame = ttk.Frame(ventana, padding=(12, 6))
list_frame.grid(row=1, column=0, sticky="nsew")
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
list_frame.rowconfigure(0, weight=1)
list_frame.columnconfigure(0, weight=1)

treeview = ttk.Treeview(list_frame,
                        columns=("nombre", "especialidad", "genero", "años de experiencia", "hospital"),
                        show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("especialidad", text="Especialidad")
treeview.heading("genero", text="Genero")
treeview.heading("años de experiencia", text="Años de experiencia")
treeview.heading("hospital", text="Hospital")
treeview.column("nombre", width=220)
treeview.column("especialidad", width=120, anchor="center")
treeview.column("genero", width=100, anchor="center")
treeview.column("años de experiencia", width=120, anchor="center")
treeview.column("hospital", width=130, anchor="center")

scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=treeview.yview)
scroll_y.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scroll_y.set)

# Ejecutar
cargar_desde_archivo()
ventana.mainloop()