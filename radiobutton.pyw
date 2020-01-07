from tkinter import *

root=Tk()

def imprimir():
	#print(varOpcion.get())
	if(varOpcion.get()==1):
		etiqueta.config(text="Masculino")
	elif:
		etiqueta.config(text="Femenino")
	else:
		etiqueta.config(text="Otras")

varOpcion=IntVar()
Label(root, text="Género: ").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()