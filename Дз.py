import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)

for i in range(50):
    turtle.color(random.choice(colors))
    turtle.pensize(random.randint(1, 10))
    turtle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.circle(random.randint(10, 100))

turtle.done()
