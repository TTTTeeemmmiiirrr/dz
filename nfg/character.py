from а.character import Character
from colorama import Fore, Style


class Berserk(Character):
    def __init__(self, name='', health=70, damage=14, color=Fore.LIGHTGREEN_EX):
        Character.__init__(self, name, health, damage, color)
        self.max_health = health

    def get_additional_damage(self):
        additional_damage = int(self.damage * (1 - self.health / self.max_health))

    def attack(self, target):
        target.take_damage(self.damage + self.get_additional_damage)

   def get_stars(self):
        return \
            f'{self.color}' \
            f'name: {self.name}\n' \
            f'health: {self.health}\n' \
            f'damage: {self.damage} (+{self.get_additional_damage()})\n' \
            f'defence: {self.defence}\n' \
            f'{Style.RESET_ALL}'










