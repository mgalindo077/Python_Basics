from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montania=IntVar()
rural=IntVar()

def opcionesViaje():
	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+=" Playa"
	if(montania.get()==1):
		opcionEscogida+=" Montaña"
	if(rural.get()==1):
		opcionEscogida+=" Turismo rural"

	txtResultado.config(text=opcionEscogida)

foto=PhotoImage(file="avion.png")
Label(root, image=foto, width=100, height=100).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame,text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text="Montaña", variable=montania, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text="Turismo rural", variable=rural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

txtResultado=Label(frame)
txtResultado.pack()

root.mainloop()