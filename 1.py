import turtle
import random

# функция для рисования пузыря
def draw_bubble(x, y, size, color):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

turtle.speed(0)

# настройки для рисования пузырей
num_bubbles = 10
min_size = 10
max_size = 50
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# рисование пузырей
for i in range(num_bubbles):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(min_size, max_size)
    color = random.choice(colors)
    draw_bubble(x, y, size, color)

turtle.done()
