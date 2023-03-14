from colorama import Fore, Style
import datetime


class Character:
    name = ''
    year_old = 0
    team = 0
    ball = 0
    color = Fore.LIGHTWHITE_EX

    def get_age(self):
        return datetime.date.today().year - self.birth_year

    def __init__(self, name='', year_old=0, team=0, ball=0, color=0):
        self.name = name
        self.year_old = year_old
        self.team = team
        self.ball = ball
        self.color = color

    def __str__(self):
        return self.get_stars()

    def get_stars(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Год рождения: {self.year_old}\n' \
            f'Группа: {self.team}\n' \
            f'Средний бал: {self.ball}\n' \
            f'{Style.RESET_ALL}'
