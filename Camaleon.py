import tkinter#libreria util para la GUI
import random
#ventana
ventana = tkinter.Tk()
ventana.geometry("700x350")
ventana.title("Camaleón") 
colors = ["Limegreen", "Gold", "Gray", "Royalblue", "Darkcyan", "Violet", "White", "Lightcoral"]
#funcion
def changeColor():
    randomcolors = random.choice(colors)
    ventana.config(background=randomcolors)
    clr = tkinter.Label(ventana, text = randomcolors, font="Purisa 25", width=10, height=2, fg="black", background="thistle2")
    clr.place(x = 250, y = 120)

#boton y Etiqueta
background = tkinter.Label(ventana, text = "Back ground color:",font = "cambria 25", width=20, height=1, fg="white", bg="black")
background.place(x = 175, y = 20)
boton = tkinter.Button(ventana, text = "Click me!",width=10, height=2, command = changeColor)
boton.place(x = 300, y = 250)

ventana.mainloop()
