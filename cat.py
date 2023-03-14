import turtle

# Инициализация черепашки
t = turtle.Turtle()
t.pensize(5)

# Нарисовать тело кота
t.color("black", "orange")
t.begin_fill()
t.goto(-100,0)
t.right(90)
t.forward(60)
t.left(90)
t.circle(-30, 180)
t.left(90)
t.forward(60)
t.end_fill()

# Нарисовать голову кота
t.color("black", "white")
t.begin_fill()
t.left(90)
t.forward(40)
t.right(90)
t.circle(40)
t.end_fill()

# Нарисовать уши кота
t.color("black", "orange")
t.begin_fill()
t.left(90)
t.forward(80)
t.right(150)
t.forward(40)
t.right(60)
t.forward(40)
t.right(150)
t.forward(80)
t.end_fill()

# Нарисовать глаза кота
t.color("black", "black")
t.up()
t.goto(-30,60)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

t.up()
t.goto(30,60)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

# Нарисовать нос и усы кота
t.color("black", "pink")
t.up()
t.goto(0,20)
t.down()
t.begin_fill()
t.circle(7)
t.end_fill()

t.color("black")
t.up()
t.goto(-15,40)
t.down()
t.right(90)
t.forward(10)

t.up()
t.goto(15,40)
t.down()
t.forward(10)

# Нарисовать хвост кота
t.color("black", "orange")
t.up()
t.goto(-100,0)
t.right(60)
t.forward(50)
t.left(120)
t.down()
t.begin_fill()
t.circle(-30, 180)
t.end_fill()

# Остановить рисование и скрыть черепашку
t.hideturtle()

# Ждать клика мыши для выхода из окна
turtle.exitonclick()
