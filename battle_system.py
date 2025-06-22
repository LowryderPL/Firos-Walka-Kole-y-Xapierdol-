import random

class Player:
    def __init__(self, name, hp, attack, defense, skills=[]):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.skills = skills

    def take_damage(self, dmg):
        reduced = max(0, dmg - self.defense)
        self.hp -= reduced
        return reduced

    def is_alive(self):
        return self.hp > 0

def simulate_battle(player, enemy):
    print(f"\n=== Rozpoczyna się walka {player.name} vs {enemy.name} ===")
    round_num = 1
    while player.is_alive() and enemy.is_alive():
        print(f"\n-- Tura {round_num} --")
        dmg_to_enemy = enemy.take_damage(player.attack)
        dmg_to_player = player.take_damage(enemy.attack)
        print(f"{player.name} zadaje {dmg_to_enemy} DMG | {enemy.name} HP: {enemy.hp}")
        print(f"{enemy.name} zadaje {dmg_to_player} DMG | {player.name} HP: {player.hp}")
        round_num += 1

    if player.is_alive():
        print(f"\n🏆 {player.name} wygrał!")
    else:
        print(f"\n💀 {enemy.name} pokonał {player.name}.")

def duel_mode():
    print("\n=== Tryb Pojedynku PvP ===")
    name1 = input("Imię gracza 1: ")
    name2 = input("Imię gracza 2: ")
    p1 = Player(name1, 120, 25, 10)
    p2 = Player(name2, 100, 30, 5)
    simulate_battle(p1, p2)

def boss_fight_mode():
    print("\n=== Tryb PvE: Walka z Bossem ===")
    name = input("Twoje imię: ")
    player = Player(name, 150, 28, 12)
    boss = Player("Król Czaszek", 250, 35, 10)
    simulate_battle(player, boss)
