
# coding: utf-8
# Rozszerzony system Craftingu dla Firos: Magic & Magic – zintegrowany z inventory i menu

import random
import time

class CraftingSystem:
    def __init__(self, user_data):
        self.user_data = user_data
        self.daily_craft_limit = 3
        self.crafting_log = {}

    def can_craft(self, user_id):
        today = time.strftime("%Y-%m-%d")
        if user_id not in self.crafting_log:
            self.crafting_log[user_id] = {}
        if today not in self.crafting_log[user_id]:
            self.crafting_log[user_id][today] = 0
        return self.crafting_log[user_id][today] < self.daily_craft_limit

    def register_craft(self, user_id):
        today = time.strftime("%Y-%m-%d")
        self.crafting_log[user_id][today] += 1

    def get_crafting_cost(self, rarity):
        # Cena w TON za próbę craftingu według rzadkości
        cost_map = {
            'common': 0.2,
            'uncommon': 0.4,
            'rare': 0.6,
            'epic': 0.8,
            'legendary': 1.0,
            'mythic': 3.0
        }
        return cost_map.get(rarity, 1.0)

    def attempt_craft(self, user_id, materials, rarity):
        if not self.can_craft(user_id):
            return {"success": False, "message": "Limit craftów dziennych osiągnięty."}

        success_chance = {
            'common': 95,
            'uncommon': 85,
            'rare': 70,
            'epic': 55,
            'legendary': 40,
            'mythic': 25
        }.get(rarity, 50)

        # Opłata TON (tu tylko zwracamy koszt, a nie wykonujemy płatności)
        ton_required = self.get_crafting_cost(rarity)

        roll = random.randint(1, 100)
        self.register_craft(user_id)

        if roll <= success_chance:
            item = f"{rarity.capitalize()} Item"
            return {
                "success": True,
                "item": item,
                "ton_cost": ton_required,
                "message": f"Crafting udany! Stworzono: {item}"
            }
        else:
            # Przypadkowa nagroda pocieszenia
            consolation = random.choice([
                "Złom", "Losowa mikstura", "Fragment legendy", "Szansa na misję bonusową"
            ])
            return {
                "success": False,
                "ton_cost": ton_required,
                "message": f"Crafting nieudany. Otrzymujesz nagrodę pocieszenia: {consolation}"
            }

# Przykład integracji (np. w menu.py albo inventory.py):
# from crafting_logic import CraftingSystem
# crafting = CraftingSystem(user_data)
# result = crafting.attempt_craft(user_id, materials, 'epic')
