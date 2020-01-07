from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="mouse.gif")
Label(miFrame, image=miImagen).place(x=50, y=50)

miLabel = Label(miFrame, text="Esta es una prueba")
miLabel.place(x=100, y=200)

Label(miFrame, text="Otra manera sin declaracion", fg="blue", font=(18)).place(x=100, y=230)

root.mainloop()