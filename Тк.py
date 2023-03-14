from tkinter import *
import random

root = Tk()
root.title("Мой радужный бот")


# функция для изменения цвета фона и кнопки
def change_colors():
    # список цветов радуги
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    # выбираем случайный цвет из списка
    random_color = random.choice(colors)
    # изменяем цвет фона
    root.configure(bg=random_color)
    # изменяем цвет кнопки
    button.configure(bg=random_color)
    # изменяем цвет текста на случайный
    text_label.configure(fg=random.choice(colors))


# создаем кнопку
button = Button(root, text="Нажми меня", command=change_colors, bg="white", fg="black")
button.pack(pady=20)

# создаем метку для вывода текста
text_label = Label(root, text="Привет", font=("Arial", 24), bg="white", fg="black")
text_label.pack(pady=50)

# изменяем размер окна
root.geometry("500x500")

root.mainloop()
