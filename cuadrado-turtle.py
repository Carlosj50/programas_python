import turtle

window1 = turtle.Screen()


cuadrado = turtle.Turtle()
for i in range(4):
    cuadrado.forward(100)
    cuadrado.left(90)
for i in range(4):
    cuadrado.forward(90)
    cuadrado.left(90)
for i in range(4):
    cuadrado.forward(80)
    cuadrado.left(90)
for i in range(4):
    cuadrado.forward(70)
    cuadrado.left(90)
turtle.mainloop()
