import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")

mi_tortuga = turtle.Turtle()
mi_tortuga.color("black")
mi_tortuga.speed(2)

mi_tortuga.penup()
mi_tortuga.goto(-100, 0)
mi_tortuga.pendown()
mi_tortuga.write("¡Hola Mundo!", font=("Arial", 24, "normal"))

turtle.done()
