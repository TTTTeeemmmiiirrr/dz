from colorama import Fore, Style


class Person:
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f"{Fore.BLUE}_._|{self.name}|_._{Style.RESET_ALL}\nЗдоровье: {Fore.LIGHTCYAN_EX}{self.health}{Style.RESET_ALL}\nНастроение: {Fore.MAGENTA}{self.mood}{Style.RESET_ALL}\nДеньги: {Fore.LIGHTGREEN_EX}{round(self.money)}{Style.RESET_ALL} "

    def do(self, person_activ):
        if type(person_activ) == Action:
            self.health += person_activ.health
            self.mood += person_activ.mood
            self.money += person_activ.money
        elif type(person_activ) == Work:
            self.health += person_activ.health
            self.mood += person_activ.mood
            self.money += person_activ.money
            if self.mood > 90:
                self.money *= 1.1
        elif type(person_activ) == Rest:
            self.health += person_activ.health
            self.mood += person_activ.mood
            self.money += person_activ.money
            if self.health < 40:
                self.mood *= 0.8


class Action:
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money


class Work(Action):
    pass


class Rest(Action):
    pass


person = Person(name='George', money=0, mood=100, health=100)
print(person)

go_to_park = Action(name='парк', money=0, mood=15, health=3)
go_to_factory = Work(name='завод', money=50, mood=-10, health=-3)
go_to_hospital = Action(name='больницa', money=-20, mood=-5, health=20)
go_to_club = Rest(name='клуб', money=-50, mood=25, health=-10)

activity_list = [go_to_park, go_to_factory, go_to_hospital, go_to_club]


for activity in activity_list:
    person.do(activity)
    print(f'{person}\n   ')
