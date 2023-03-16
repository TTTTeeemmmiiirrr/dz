from а.character import Character
from colorama import Fore

player1 = Character(name='eror', health=70, damage=14, color=Fore.LIGHTGREEN_EX)
print(player1.get_stars())

player2 = Character(name='erorchik', health=100, damage=13, color=Fore.LIGHTYELLOW_EX)
print(player2.get_stars())

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    print(player2)
    if not player2.is_alive():
        break
    player2.attack(player1)
    print(player1)

print('Игра окончена')
if player1.is_alive():
    print(f'{player1.name} победил!')
else:
    print(f'{player2.name} победил!')


player1.attack(player2)

print(player1)
print(player2)