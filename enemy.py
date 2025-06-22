# enemy.py — Firos: Magic & Magic

class Enemy:
    def __init__(self, name, hp, power, rarity="common"):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power
        self.rarity = rarity

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self):
        return self.power

    def __str__(self):
        return f"{self.name} [HP: {self.hp}/{self.max_hp}, Siła: {self.power}]"
