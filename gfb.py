my_list = ["Книга", "Кофе", "Напиток", "Парк"]

while True:
    user = input("Введите слово или 0 для выхода: ")
    if user == "0":
        break
    elif user in my_list:
        print("Слово найдено в списке!")
    else:
        print("Слово не найдено в списке.")
