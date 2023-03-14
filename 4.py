from character1 import Character
from colorama import Fore
   #Имена придумывал не я, а мой друг
player1 = Character(name='Абобус Амогус Амогусавич', year_old=2005, team=1, ball=1, color=Fore.LIGHTBLUE_EX)
print(player1.get_stars())

player2 = Character(name='Нани', year_old=2002, team=5, ball=8, color=Fore.BLUE)
print(player2.get_stars())

player3 = Character(name='Саша', year_old=2012, team=5, ball=12, color=Fore.LIGHTCYAN_EX)
print(player3.get_stars())

player4 = Character(name='цувтуервфн', year_old=2007, team=2, ball=10, color=Fore.LIGHTYELLOW_EX) #Это имя английское просто написано на руском
print(player4.get_stars())


print(player1.get_age())

