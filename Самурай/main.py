from Самурай.character import Character, Samurai
from colorama import Fore

player1 = Samurai(name='Hattori', health=100, damage=10, color=Fore.LIGHTRED_EX, defence=10)
player2 = Character(name='Enemy', health=100, damage=15, color=Fore.LIGHTGREEN_EX)

for i in range(6):
    player1.attack(player2)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    print(player2.get_stars())
    if not player2.is_alive():
        break
    player2.attack(player1)
    print(player1.get_stars())

print('Игра окончена')
if player1.is_alive():
    print(f'{player1.name} победил!')
else:
    print(f'{player2.name} победил!')
