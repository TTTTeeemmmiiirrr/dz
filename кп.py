import turtle

# Встановлення вікна
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("white")

# Створення черепашки
t = turtle.Turtle()
t.pensize(3)

# Налаштування кольорів
t.pencolor("pink")
t.fillcolor("red")

# Початок малювання
t.begin_fill()
t.left(45)
t.forward(150)
t.circle(75, 180)
t.right(90)
t.circle(75, 180)
t.forward(150)
t.end_fill()

# Закриття вікна
turtle.done()
