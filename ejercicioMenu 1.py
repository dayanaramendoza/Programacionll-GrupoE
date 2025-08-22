import tkinter as tk
from tkinter import messagebox
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("SISTEMA DE REGISTRO DE PACIENTES")
ventanaPrincipal.geometry("600x600")
ventanaPrincipal.configure(bg="#4682B4")
#CREAR LA BARRA DE MENU
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
#MENÚ PACIENTES
menuPacientes=tk.Menu(tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo paciente", command=lambda:print(nuevoPaciente()))
menuPacientes.add_command(label="Buscar Paciente", command=lambda: print(buscarPaciente()))
menuPacientes.add_command(label="Eliminar Paciente", command=lambda: print(eliminarPaciente()))
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal)
def nuevoPaciente():
    messagebox.showinfo("Nuevo paciente", "Este es el espacio para crear nuevo paciente")
    ventanaRegistro=tk.Toplevel(ventanaPrincipal) #top level sirve para crear una nueva ventana secundaria
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry('400x400')
    ventanaRegistro.configure(bg="#B0C4DE")
    nombreLabel=tk.Label(ventanaRegistro, text="Nombre: ")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w") #n=norte, s=sur, w=oeste we=este
    nombreLabel.configure(bg="##B0C4DE")
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
#DIRECCION
    direccionLabel=tk.Label(ventanaRegistro, text="Direccion: ")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w") #n=norte, s=sur, w=oeste we=este
    direccionLabel.configure(bg="##B0C4DE")
    entrydireccion=tk.Entry(ventanaRegistro)
    entrydireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
#TELEFONO
    TelefonoLabel=tk.Label(ventanaRegistro, text="Telefono: ")
    TelefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w") #n=norte, s=sur, w=oeste we=este
    TelefonoLabel.configure(bg="##B0C4DE")
    entrytelefono=tk.Entry(ventanaRegistro)
    entrytelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
#SEXO (radiobutton)
    sexoLabel=tk.Label(ventanaRegistro, text="Sexo")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo=tk.StringVar(Value="Masculino")
    rbMasculino=tk.Radiobutton(ventanaRegistro, text="Masculino", variable="sexo", value="Masculino", bg="#B0E0E6")
    rbMasculino.grid(row=4, column=1, sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro, text="Femenino", variable="sexo", value="Femenino", bg="#B0E0E6")
    rbMasculino.grid(row=4, column=1, sticky="w")
#ENFERMEDADES BASE (RADIOBUTTON)
    enfLabel=tk.Label(ventanaRegistro, text="Enfermedad de base: ")
    enfLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    cbDiabetes=tk.Checkbutton(ventanaRegistro, text="Diabetes", variable=diabetes)
    cbDiabetes.grid(row=5, column=1, sticky="w")
    cbHipertension=tk.Checkbutton(ventanaRegistro, text="Hipertension", variable=hipertension)
    cbHipertension.grid(row=6, column=1, sticky="w")
    cbAsma=tk.Checkbutton(ventanaRegistro, text="asma", variable=asma)
    cbAsma.grid(row=6, column=1, sticky="w")
    def registrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertension")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades)>0:
            enfermedadesTexto=','.join(enfermedades)
        else:
            enfermedadesTexto="Ninguna"
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Telefono:{entrytelefono.get()}\n"
            f"sexo:{sexo.get()}\n"
            f"Enfermedades:{enfermedadesTexto}"
        )
        messagebox.showinfo("Datos registrados", info)
        ventanaRegistro.destroy()
    btnRegistrar = tk.Button(ventanaRegistro, text="Datos registrados", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, pady=10, columnspan=2, pady=15)
def buscarPaciente():
    messagebox.showinfo("Buscar paciente", "Este es el espacio para buscar algún paciente")
def eliminarPaciente():
    messagebox.showinfo("Eliminar paciente", "Este es el espacio para eliminar algún paciente")   
#MENU DOCTORES
menuDoctores=tk.Menu(tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo doctor", command=lambda:print(nuevoDoctor()))
menuDoctores.add_command(label="Buscar Doctor", command=lambda: print(buscarDoctor()))
menuDoctores.add_command(label="Eliminar Doctor", command=lambda: print(eliminarDoctor()))
def nuevoDoctor():
    messagebox.showinfo("Nuevo doctor", "Este es el espacio para crear nuevo doctor")
    ventanaRegistro = tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Doctor")
    ventanaRegistro.geometry('600x600')
    ventanaRegistro.configure(bg="#B0C4DE")
#NOMBRE
    nombreLabel1 = tk.Label(ventanaRegistro, text="Nombre completo:")
    nombreLabel1.configure(bg="#B0C4DE")
    nombreLabel1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entryNombre1 = tk.Entry(ventanaRegistro)
    entryNombre1.grid(row=0, column=1, padx=10, pady=5, sticky="we")
#DIRECCION
    direccionLabel1 = tk.Label(ventanaRegistro, text="Direccion: ")
    direccionLabel1.configure(bg="#B0C4DE")
    direccionLabel1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entryDireccion1 = tk.Entry(ventanaRegistro)
    entryDireccion1.grid(row=1, column=1, padx=10, pady=5, sticky="we")
 # TELÉFONO
    telefonoLabel1 = tk.Label(ventanaRegistro, text="Telefono:")
    telefonoLabel1.configure(bg="#B0C4DE")
    telefonoLabel1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entryTelefono1 = tk.Entry(ventanaRegistro)
    entryTelefono1.grid(row=2, column=1, padx=10, pady=5, sticky="we")
 #ESPECIALIDAD
    especialidadLabel = tk.Label(ventanaRegistro, text="Especialidad")
    especialidadLabel.configure(bg="#B0C4DE")
    especialidadLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    especialidad=tk.StringVar(value="Pediatria")
    rbPediatria=tk.Radiobutton(ventanaRegistro, text= "Pediatria", variable=especialidad, value="Pediatria", bg="#B0C4DE")
    rbPediatria.grid(row=3, column=1, sticky="w")
    rbCardiologia=tk.Radiobutton(ventanaRegistro, text= "Cardiologia", variable=especialidad, value="Cardiologia", bg="#B0C4DE")
    rbCardiologia.grid(row=3, column=2, sticky="w")
    rbNeurologia=tk.Radiobutton(ventanaRegistro, text= "Neurologia", variable=especialidad, value="Neurologia", bg="#B0C4DE")
    rbNeurologia.grid(row=3, column=3, sticky="w")
#DISPONIBILIDAD
    dispoLabel = tk.Label(ventanaRegistro, text="Diponibilidad", bg="#B0C4DE")
    dispoLabel.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    mañana = tk.BooleanVar()
    tarde = tk.BooleanVar()
    noche = tk.BooleanVar()
    cbMañana = tk.Checkbutton(ventanaRegistro, text="Mañana", variable=mañana, bg="#B0C4DE")
    cbMañana.grid(row=4, column=1, sticky="w")
    cbTarde = tk.Checkbutton(ventanaRegistro, text="tarde", variable=tarde, bg="#B0C4DE")
    cbTarde.grid(row=5, column=1, sticky="w")
    cbnoche = tk.Checkbutton(ventanaRegistro, text="noche", variable=noche, bg="#B0C4DE")
    cbnoche.grid(row=6, column=1, sticky="w")
 # FUNCIÓN GUARDAR
    def registrarDoctor():
        Disponiblidad = []
        if mañana.get(): Disponiblidad.append("Mañana")
        if tarde.get(): Disponiblidad.append("Tarde")
        if noche.get(): Disponiblidad.append("noche")
        DisponibilidadTexto = ', '.join(Disponiblidad) if Disponiblidad else "Ninguna"
        info1 = (
            f"Nombre: {entryNombre1.get()}\n"
            f"Direccion: {entryDireccion1.get()}\n"
            f"Telefono: {entryTelefono1.get()}\n"
            f"Especialidad: {especialidad.get()}\n"
            f"Disponibilidad: {DisponibilidadTexto}"
            )
        messagebox.showinfo("Datos Registrados", info1)
        ventanaRegistro.destroy()
    btnGuardar = tk.Button(ventanaRegistro, text="Registrar", command=registrarDoctor)
    btnGuardar.grid(row=7, column=1, pady=10)
def buscarDoctor():
    messagebox.showinfo("Buscar Doctor", "Este es el espacio para buscar algún doctor")
def eliminarDoctor():
    messagebox.showinfo("Eliminar Doctor", "Este es el espacio para elininar algún doctor") 
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal)
#MENÚ AYUDA
menuAyuda= tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Version 1.0 - Sistema Biomedicina"))

ventanaPrincipal.mainloop()