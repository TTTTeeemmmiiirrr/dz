import time

from а.character import Character
import random


class Assassin(Character):
    def __init__(self, name='', health=80, damage=10,):
        Character.__init__(self, name, health, damage,)

    def attack(self, target):
        if random.randint(1, 100) <= 20:
            target.take_damage(1000)
            if not target.is_alive():
                return
        target.take_damage(self.damage)
        if not target.is_alive():
            return
        print(f'{self.name} атакует {target.name}')
        time.sleep(1)

    def get_stars(self):
        return \
            f'{self.color}' \
            f'name: {self.name}\n' \
            f'health: {self.health}\n' \
            f'damage: {self.damage}\n' \
            f'defence: {self.defence}\n' \


    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)

    def is_alive(self):
        return self.health > 0

