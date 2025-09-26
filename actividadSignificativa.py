import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
#CREAR VENTANA PRINCIPAL
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("1000x800")
#LISTA DE PACIENTES (INICIALMENTE VACIA)
paciente_data=[]
#FUNCION PARA ENMASCARAR FECHA
def enmascarar_fecha(texto):
   limpio=''.join(filter(str.isdigit, texto))
   formato_final=""
   if len(limpio)>8:
       limpio=limpio[:8]
   if len(limpio)>4:
      formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
   elif len(limpio)>2:
       formato_final=f"{limpio[:2]}-{limpio[2:]}"
   else:
       formato_final=limpio
   if fechaN.get()!=formato_final:
       fechaN.delete(0,tk.END)
       fechaN.insert(0, formato_final)

       if len(fechaN.get())==10:
           fecha_actual=datetime.now().date()
           fecha_nacimiento=datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
           edad=fecha_actual.year-fecha_nacimiento.year
           edadVar.set(edad)
       else:
           edadVar.set("")
       return True
#GUARDAR LOS REGISTROS EN UN ARCHIVO DE TEXTO
def guardar_en_archivo():
   with open("pacientePeso.txt","w", encoding="utf-8") as archivo:
       for paciente in paciente_data:
           archivo.write(
               f"{paciente['Nombre']}|"
               f"{paciente['Fecha de Nacimiento']}|"
               f"{paciente['Edad']}|"
               f"{paciente['Peso']}|"
               f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
               f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}\n"
           )
            
def cargar_desde_archivo_paciente():
   try:
       with open("pacientePeso.txt", "r", encoding="utf-8") as archivo:
           paciente_data.clear()
           for linea in archivo:
               datos=linea.strip().split("|")
               if len(datos)==8:
                   paciente= {
                       "Nombre": datos[0],
                       "Fecha de Nacimiento": datos[1],
                       "Edad": datos[2],
                       "Genero": datos[3],
                       "Peso": datos[4],
                       "Grupo Sanguineo": datos[5],
                       "Tipo de Seguro": datos[6],
                       "Centro Medico": datos[7]
                   }
               paciente_data.append(paciente)
       cargar_treeview()
   except FileNotFoundError:
       open("pacientePeso.txt", "w", encoding="utf-8").close()

#FUNCION ELIMINAR PACIENTE
def eliminar_paciente():
   seleccionado= treeview.selection()
   if seleccionado:
       indice=int(seleccionado[0])
       id_item=seleccionado[0]
       if messagebox.askyesno("Eliminar Paciente", f"¿Está seguro de eliminar al paciente '{treeview.item(id_item, 'values')[0]}'?"):
           del paciente_data[indice]
           guardar_en_archivo() # GUARDAR LOS CAMBIOS EN EL ARCHIVO
           cargar_treeview()
           messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente.")
       else: #este else es del if seleccionado
           messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningun paciente.")
           return

#FUNCION PARA REGITRAR PACIENTE
def registrar_paciente():
   paciente={  #Crear un diccionario con los datos registrados
       "Nombre": nombreP.get(),
       "Fecha de Nacimiento": fechaN.get(),
       "Edad": edadVar.get(),
       "Genero": genero.get(),
       "Peso": Peso.get(),
       "Grupo Sanguineo": entryGrupoSanguineo.get(),
       "Tipo de Seguro": tipo_seguro.get(),
       "Centro Medico": centro_medico.get()
   }
#AGREGAR PACIENTE A LA LISTA
   paciente_data.append(paciente)
   guardar_en_archivo()
   cargar_treeview()
#CARGAR EL TREEVIEW
def cargar_treeview():
    #limpiar el treeview
   for paciente in treeview.get_children():
       treeview.delete(paciente)
    #Insertar cada paciente
   for i, item in enumerate(paciente_data):
       treeview.insert(
           "", "end", iid=str(i),
           values=(
               item["Nombre"],
               item["Fecha de Nacimiento"],
               item["Edad"],
               item["Genero"],
               item["Peso"],
               item["Grupo Sanguineo"],
               item["Tipo de Seguro"],
               item["Centro Medico"],

           )
       )
#CREAR CONTENEDOR NOTEBOOK (PESTAÑAS)
pestañas=ttk.Notebook(ventana_principal)
#CREAR FRAMES (UNO POR PESTAÑA)
frame_pacientes=ttk.Frame(pestañas)
#AGREGAR PESTAÑAS AL NOTEBOOK
pestañas.add(frame_pacientes, text="Pacientes")
#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")
#NOMBRE
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)
#FECHA DE NACIMIENTO
validacion_fecha=ventana_principal.register(enmascarar_fecha)
labelFechaN=tk.Label(frame_pacientes, text="Fecha de nacimiento: ")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
fechaN=ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)
#EDAD
edadVar=tk.StringVar()
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
EdadP=tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
EdadP.grid(row=2, column=1, padx=5, pady=5, sticky="w")
#GENERO
labelGenero=tk.Label(frame_pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5)
genero=tk.StringVar()
genero.set("Masculino") #VALOR POR DEFECTO
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5)
#PESO 
PesoVar=tk.StringVar()
labelPeso=tk.Label(frame_pacientes, text="Peso (en kg): ")
labelPeso.grid(row=4, column=0, sticky="w", pady=5, padx=5)
Peso=tk.Entry(frame_pacientes, textvariable=PesoVar)
Peso.grid(row=4, column=1, padx=5, pady=5, sticky="w")
#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo: ")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#TIPO DE SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro: ")
labelTipoSeguro.grid(row=6, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #VALOR POR DEFECTO
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", pady=5, padx=5)
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud: ")
labelCentroMedico.grid(row=7, column=0, sticky="w", pady=5, padx=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")
#BOTON REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrar_paciente)
btn_registrar.grid(row=0, column=0, padx=5)
#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command=eliminar_paciente)
btn_eliminar.grid(row=0, column=1, padx=5)
#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "Peso", "GrupoS", "TipoS", "CentroM"), show="headings")
#DEFINIR ENCABEZADOS
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Peso", text="Peso")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=80, anchor="center")
treeview.column("Peso", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#SCROLLBAR VERTICAL
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")
cargar_desde_archivo_paciente()
ventana_principal.mainloop()