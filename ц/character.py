from colorama import Fore, Style


class Samurai(Character):
    def __init__(self, name='', health=100, damage=10, color=Fore.LIGHTRED_EX):
        Character.__init__(self, name, health, damage, color)
        self.max_multiplier = 5
        self.attack_multiplier = 0

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


player1 = Samurai(name='Hattori', health=100, damage=10, color=Fore.LIGHTRED_EX)
player2 = Character(name='Enemy', health=100, damage=15, color=Fore.LIGHTGREEN_EX)

for i in range(6):
    player1.attack(player2)

print(player2.get_stars())


class Character:
    pass