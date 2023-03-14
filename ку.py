import turtle
import random

# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

# Функция для рисования лепестков
def draw_petal(radius):
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)

# Функция для рисования цветка
def draw_flower():
    # Рисуем лепестки
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(6):
        t.color(random.choice(colors))
        draw_petal(50)
        t.left(60)
    # Рисуем середину
    t.color("yellow")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# Настройки черепашки
t.speed(0)  # Максимальная скорость
t.pensize(3)  # Толщина линии

# Рисуем цветок
draw_flower()

# Завершение программы при клике
screen.exitonclick()
