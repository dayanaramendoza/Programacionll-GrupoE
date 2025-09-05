import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
#CREAR VENTANA PRINCIPAL
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("1000x800")
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
#LISTA DE PACIENTES (INICIALMENTE VACIA)
paciente_data=[]
#FUNCION PARA REGITRAR PACIENTE
def registrar_paciente():
    paciente={  #Crear un diccionario con los datos registrados
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(),
        "Grupo Sanguineo": entryGrupoSanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Medico": centro_medico.get()
    }
    #AGREGAR PACIENTE A LA LISTA
    paciente_data.append(paciente)
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
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"]
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
#CREAR FRAMES (DOCTORES)
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
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
#GRUPO SANGUINEO
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo: ")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=4, column=1, sticky="w", pady=5, padx=5)
#TIPO DE SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro: ")
labelTipoSeguro.grid(row=5, column=0, sticky="w", pady=5, padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #VALOR POR DEFECTO
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", pady=5, padx=5)
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud: ")
labelCentroMedico.grid(row=6, column=0, sticky="w", pady=5, padx=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")
#BOTON REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrar_paciente)
btn_registrar.grid(row=0, column=0, padx=5)
#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, padx=5)
#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")
#DEFINIR ENCABEZADOS
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#SCROLLBAR VERTICAL
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")
#FRAME DOCTORES
#NOMBRE
labelNombreD=tk.Label(frame_doctores, text="Nombre: ")
labelNombreD.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=0, column=1, sticky="w", padx=5, pady=5)
#ESPECIALIDAD
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad: ")
labelEspecialidad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
Especialidad=tk.StringVar()
Especialidad.set("Cardiología") #VALOR POR DEFECTO
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Pediatría", "Neurología", "Traumatología", "Oftalmología"], textvariable=Especialidad)
comboEspecialidad.grid(row=2, column=1, sticky="w", pady=5, padx=5)
#EDAD
labelEdadD=tk.Label(frame_doctores, text="Edad: ")
labelEdadD.grid(row=3, column=0, sticky="w", pady=5, padx=5)
valores=list(range(25, 81))
edadD=tk.Spinbox(frame_doctores, values=(valores))
edadD.grid(row=3, column=1, padx=10, pady=10, sticky="w")
#TELEFONO
labelTelefono=tk.Label(frame_doctores, text="Telefono: ")
labelTelefono.grid(row=4, column=0, sticky="w", padx=5, pady=5)
Telefono=tk.Entry(frame_doctores)
Telefono.grid(row=4, column=1, sticky="w", padx=5, pady=5)
#Frame para los botones
boton_frame=tk.Frame(frame_doctores)
boton_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky="w")
#BOTON REGISTRAR
boton_registrar=tk.Button(boton_frame, text="Registrar", command="")
boton_registrar.grid(row=5, column=0, padx=5)
boton_registrar.configure(background="green")
#BOTON ELIMINAR
boton_eliminar=tk.Button(boton_frame, text="Eliminar", command="")
boton_eliminar.grid(row=5, column=1, padx=5)
boton_eliminar.configure(background="red")
#CREAR TREEVIEW PARA MOSTRAR DOCTORES
TreevieW=ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
#DEFINIR ENCABEZADOS
TreevieW.heading("Nombre", text="Nombre Completo")
TreevieW.heading("Especialidad", text="Especialidad")
TreevieW.heading("Edad", text="Edad")
TreevieW.heading("Telefono", text="Telefono")
#DEFINIR ANCHOS DE COLUMNAS
TreevieW.column("Nombre", width=120)
TreevieW.column("Especialidad", width=120)
TreevieW.column("Edad", width=50, anchor="center")
TreevieW.column("Telefono", width=60, anchor="center")
#UBICAR EL TREEVIEW EN LA CUADRICULA
TreevieW.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5, pady=10)
#SCROLLBAR VERTICAL
Scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=TreevieW.yview)
TreevieW.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=6, column=2, sticky="ns")
ventana_principal.mainloop()