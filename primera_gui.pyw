from tkinter import *

raiz=Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(True,False) #Permitir cambiiar el ancho,alto de una ventana
raiz.iconbitmap("CV pic.ico") #Colocar icono de ventana conversor.ico //google
#raiz.geometry("650x350")
raiz.config(bg="blue")
raiz.config(cursor="pirate")

miFrame=Frame()
miFrame.pack(side="left", anchor="n", fill="both", expand="True")
miFrame.config(bg="light grey")
miFrame.config(width="650", height="350")
#miFrame.config(bd=35)
#miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")

lblMensaje = Label(miFrame,text="Esta es una prueba")

raiz.mainloop()