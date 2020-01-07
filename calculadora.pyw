from tkinter import *
#----------operaciones algebraicas

def restar():
	numeroPantalla.set(str(operador1-operador2))

def multiplicar():
	numeroPantalla.set(str(operador1*operador2))

def dividir():
	if(operador2!=0):
		numeroPantalla.set(str(operador1*operador2))

#----------pulsaciones teclado
def numeroPulsado(valorPulsado):
	global operacion

	if (operacion!=""):
		numeroPantalla.set(valorPulsado)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get()+str(valorPulsado))

def suma(num):
	global operacion
	global resultado

	resultado += int(num)
	operacion="suma"
	numeroPantalla.set(resultado)

#------------funcion el resultado
def el_resultado():
	global resultado

	numeroPantalla.set(resultado+int(numeroPantalla.get()))

	resultado=0


def Operacion(valorPulsado):
	operacion=valorPulsado

	global operador1

	if(operador1==0):
		operador1 = int(numeroPantalla.get())
	else:
		operador2 = int(numeroPantalla.get())
		numeroPantalla.set("0")	

		if(operacion=="sumar"):
			numeroPantalla.set(str(sumar()))
		elif(operacion=="restar"):
			numeroPantalla.set(str(restar()))
		elif(operacion=="multiplicar"):
			numeroPantalla.set(str(multiplicar()))
		elif(operacion=="dividir" and operador2!=0):
			numeroPantalla.set(str(dividir()))

		operacion=""
#---------------

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
operacion=""
resultado=0

#-------------Pantalla
numeroPantalla=StringVar()
numeroPantalla.set("0")

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#----------fila1
boton7 = Button(miFrame,text="7", width=3, command=lambda:numeroPulsado(7)).grid(row=2,column=1)
boton8 = Button(miFrame,text="8", width=3, command=lambda:numeroPulsado(8)).grid(row=2,column=2)
boton9 = Button(miFrame,text="9", width=3, command=lambda:numeroPulsado(9)).grid(row=2,column=3)
botonDiv = Button(miFrame,text="/", width=3, command=lambda:Operacion("dividir")).grid(row=2,column=4)

#----------fila2
boton4 = Button(miFrame,text="4", width=3, command=lambda:numeroPulsado(4)).grid(row=3,column=1)
boton5 = Button(miFrame,text="5", width=3, command=lambda:numeroPulsado(5)).grid(row=3,column=2)
boton6 = Button(miFrame,text="6", width=3, command=lambda:numeroPulsado(6)).grid(row=3,column=3)
botonMult = Button(miFrame,text="X", width=3, command=lambda:Operacion("multiplicar")).grid(row=3,column=4)

#----------fila3
boton1 = Button(miFrame,text="1", width=3, command=lambda:numeroPulsado(1)).grid(row=4,column=1)
boton2 = Button(miFrame,text="2", width=3, command=lambda:numeroPulsado(2)).grid(row=4,column=2)
boton3 = Button(miFrame,text="3", width=3, command=lambda:numeroPulsado(3)).grid(row=4,column=3)
botonRest = Button(miFrame,text="-", width=3, command=lambda:Operacion("restar")).grid(row=4,column=4)

#----------fila4
boton0 = Button(miFrame,text="0", width=3, command=lambda:numeroPulsado(0)).grid(row=5,column=1)
botonComa = Button(miFrame,text=",", width=3).grid(row=5,column=2)
botonIgual = Button(miFrame,text="=", width=3, command=lambda:el_resultado()).grid(row=5,column=3)
botonSuma = Button(miFrame,text="+", width=3, command=lambda:suma(numeroPantalla.get())).grid(row=5,column=4)







raiz.mainloop()