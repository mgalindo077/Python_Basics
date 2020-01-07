from tkinter import *
from tkinter import messagebox # Ventanas emergentes

root=Tk()

def infoAdicional():
	messagebox.showinfo("Acerca de", "Procesador de textos version 2019")

def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def SalirApp():
	#valor=messagebox.askquestion("Salir?","Deseas salir de la aplicación?")
	#if(valor=="yes"):
	#	root.destroy()
	valor=messagebox.askokcancel("Salir?","Deseas salir de la aplicación?")

	if(valor==True):
		root.destroy()

def cerrarDocto():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar documento, bloqueado")
	if valor==False:
		root.destroy()


root.title("Ejemplo")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocto)
archivoMenu.add_command(label="Salir", command=SalirApp)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Acerca de ", command=infoAdicional)
archivoAyuda.add_command(label="Licencia ", command=avisoLicencia)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




root.mainloop()