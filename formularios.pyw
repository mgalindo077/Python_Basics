from tkinter import *

raiz = Tk()

miFrame=Frame(raiz,width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
Label(miFrame, text="Nombre: ").grid(row=0, column=0, sticky="e")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)
Label(miFrame, text="Apellido: ").grid(row=1, column=0, sticky="e")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1)
Label(miFrame, text="Direccion de Casa: ").grid(row=2, column=0, sticky="e")

raiz.mainloop()