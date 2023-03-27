from colorama import Fore, Style

from а.character import Character


class Samurai(Character):
    def __init__(self, name='', health=100, damage=10, color=Fore.LIGHTRED_EX, defence=0):
        Character.__init__(self, name, health, damage, color)
        self.max_multiplier = 0.5
        self.attack_multiplier = 0
        self.defence = defence

    def attack(self, target):
        additional_damage = int(self.damage * self.attack_multiplier)
        target.take_damage(self.damage + additional_damage)
        self.increase_attack_multiplier()

    def increase_attack_multiplier(self):
        if self.attack_multiplier < self.max_multiplier:
            self.attack_multiplier += 0.1
        else:
            self.attack_multiplier = 0

    def get_stars(self):
        return \
            f'{self.color}' \
            f'name: {self.name}\n' \
            f'health: {self.health}\n' \
            f'damage: {self.damage} (+{int(self.damage * self.attack_multiplier)})\n' \
            f'defence: {self.defence}\n' \
            f'{Style.RESET_ALL}'

    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)

    def is_alive(self):
        return self.health > 0




