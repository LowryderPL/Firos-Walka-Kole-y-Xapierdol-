import random

class Enemy:
    def __init__(self, name, hp, attack_range):
        self.name = name
        self.hp = hp
        self.attack_range = attack_range

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        return random.randint(*self.attack_range)


class Battle:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_hp = 30
        self.player_attack = (4, 8)
        self.enemy = Enemy("Upiór Cienia", 20, (3, 6))

    def start(self):
        print(f"\n🧨 Walka! {self.player_name} vs {self.enemy.name}\n")

        while self.player_hp > 0 and self.enemy.is_alive():
            print(f"Twoje HP: {self.player_hp} | {self.enemy.name} HP: {self.enemy.hp}")
            action = input("1. Atakuj\n2. Uciekaj\n> ").strip()

            if action == "1":
                dmg = random.randint(*self.player_attack)
                self.enemy.hp -= dmg
                print(f"Zadałeś {dmg} obrażeń!")
                if not self.enemy.is_alive():
                    print("✅ Pokonałeś wroga!")
                    break

                enemy_dmg = self.enemy.attack()
                self.player_hp -= enemy_dmg
                print(f"{self.enemy.name} zadał Ci {enemy_dmg} obrażeń!\n")
            elif action == "2":
                print("💨 Uciekasz z pola bitwy...")
                break
            else:
                print("Nieznana akcja.")

        if self.player_hp <= 0:
            print("💀 Zginąłeś w walce...")
