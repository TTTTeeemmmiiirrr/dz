from character import Character
from colorama import Fore

player1 = Character(name='Абобус Амогус Амогусавич', birth_year=2005, team=1, ball=1, color=Fore.LIGHTBLUE_EX)
print(player1.get_stars())

print(player1.get_age())

player2 = Character(name='Нани', birth_year=2002, team=5, ball=8, color=Fore.BLUE)
print(player2.get_stars())

print(player2.get_age())

player3 = Character(name='Саша', birth_year=2012, team=5, ball=12, color=Fore.LIGHTCYAN_EX)
print(player3.get_stars())

print(player3.get_age())

player4 = Character(name='цувтуервфн', birth_year=2007, team=2, ball=10, color=Fore.LIGHTYELLOW_EX)
print(player4.get_stars())

print(player4.get_age())
