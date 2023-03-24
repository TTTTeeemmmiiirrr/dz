from Самурай.character import Character, Samurai
from colorama import Fore

player1 = Samurai(name='Hattori', health=100, damage=10, color=Fore.LIGHTRED_EX)
player2 = Character(name='Enemy', health=100, damage=15, color=Fore.LIGHTGREEN_EX)

for i in range(6):
    player1.attack(player2)

print(player2.get_stars())
