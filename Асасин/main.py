from а.character import Character
from Асасин.character import Assassin

player1 = Assassin(name='Assassin', health=70, damage=14)
print(player1.get_stars())

player2 = Character(name='Mr Evil', health=100, damage=13)
print(player2.get_stars())

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
