from а.character import Character
from colorama import Fore

player1 = Character(name='eror', health=70, damage=2, color=Fore.LIGHTGREEN_EX)
print(player1.get_stars())

player2 = Character(name='erorchik', health=100, damage=1, color=Fore.LIGHTYELLOW_EX)
print(player2.get_stars())

player1.attack(player2)

print(player1)
print(player2)