from builtins import eval
from tkinter import*
import math
import turtle

def boton1():
    t = turtle.Pen()
    texto = int(input("Ingrese el numero de lados de la figura el numero de lados debe ser menor o igual a 5: "))
    if(texto == 3):
        t.reset()
        print("Area y perimetro de un triangulo\n")
        lado1 = int(input("Ingrese la medida del primer lado: "))
        lado2 = int(input("Ingrese la medida del primer lado: "))
        lado3 = int(input("Ingrese la medida del primer lado: "))
        
        if(lado1 + lado2 > lado3):
            if(lado1 + lado3 > lado2):
                if(lado2 + lado3 > lado1):
                    perimetro = lado1 + lado2 + lado3
                    sumap = lado1 + lado2 + lado3
                    p = sumap/2
                    area = math.sqrt(p*(p-lado1)*(p-lado2)*(p-lado3))
                    print("El perimetro es igual a: ",perimetro)
                    print("El area es igual a: ",area)
                    
            t.forward(200)
            t.left(120)
            t.forward(200)
            t.left(120)
            t.forward(200)
        
        else:
            print("Los lados ingresados NO forman un triangulo")

        

    if(texto == 4):
        t.reset()
        print("Area y perimetro de un cuadrado\n")
        lado = int(input("Ingrese la medida de los lados: "))
        perimetro = lado + lado + lado + lado
        area = lado*lado
        print("El perimetro es igual a: ", perimetro)
        print("El area es igual a: ", area)

        t.forward(lado)
        t.left(90)
        t.forward(lado)
        t.left(90)
        t.forward(lado)
        t.left(90)
        t.forward(lado)

    if(texto == 5):
        t.reset()
        print("Area y perimetro de un pentagono regular")
        lado = int(input("Ingrese la medida de los lados: "))
        perimetro = lado + lado + lado + lado + lado
        a = 360/5
        ta = 2*math.tan(a/2)
        apotema = lado/ta
        print(apotema)

        area = (perimetro*apotema)/2
        print("El perimetro es igual a:", perimetro)
        print("El area es igual a: ", area)

        t.forward(lado)
        t.right(72)
        t.forward(lado)
        t.right(72)
        t.forward(lado)
        t.right(72)
        t.forward(lado)
        t.right(72)
        t.forward(lado)
        t.right(72)

    else:
        print("Opcion incorrecta ingrese un numero valido")
        
    
    

def boton2():
    ventana2 = Tk()
    canvas2 = Canvas(ventana2, width = 640, height = 480)
    canvas2.pack()
    ventana2.mainloop()


tk = Tk()
tk.resizable(0, 0)
canvas = Canvas(tk, width = 640, height = 480, bd = 0, highlightthickness = 0)
btn1 = Button(canvas, text = "1. Calcular area y perimetro", command=lambda:boton1())
btn2 = Button(canvas, text = "2. Lluvia animacion", command=lambda:boton2())

btn1.pack()
btn2.pack()
canvas.pack()
tk.update()
tk.mainloop()
