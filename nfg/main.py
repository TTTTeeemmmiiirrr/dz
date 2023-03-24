from а.character import Character
from berserk import Berserk
from colorama import Fore

player1 = Character(name='eror', health=70, damage=14, color=Fore.LIGHTGREEN_EX)
print(player1.get_stars())

player2 = Character(name='erorchik', health=100, damage=13, color=Fore.LIGHTYELLOW_EX)
print(player2.get_stars())

