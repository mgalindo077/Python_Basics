from tkinter import *
from tkinter import messagebox # Ventanas emergentes
from tkinter import filedialog

root=Tk()


def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="c:", filetypes=(
		("Archivos de Excel","*.xlsx"),
		("Archivos de texto","*.txt"),
		("Todos los archivos","*.*")))
	print(fichero)


Button(root,text="Abrir fichero", command=abreFichero).pack()

root.mainloop()