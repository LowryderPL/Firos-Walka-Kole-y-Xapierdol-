shop.py - Pełny system sklepu FIROS: Magic & Magic

import random from inventory import Inventory from items_data import SHOP_ITEMS from currencies import player_rfm_balance, deduct_rfm

class Shop: def init(self): self.stock = [] self.refresh_stock()

def refresh_stock(self):
    """Losuje nowe przedmioty do sklepu"""
    self.stock = random.sample(SHOP_ITEMS, min(len(SHOP_ITEMS), 12))

def display_stock(self):
    print("--- Sklep FIROS ---")
    for i, item in enumerate(self.stock):
        print(f"{i+1}. {item['name']} - {item['price']} RFM")
    print("-------------------")

def buy_item(self, player_inventory, choice):
    if 1 <= choice <= len(self.stock):
        item = self.stock[choice - 1]
        if player_rfm_balance() >= item['price']:
            deduct_rfm(item['price'])
            player_inventory.add_item(item)
            print(f"Zakupiono: {item['name']}")
        else:
            print("Nie masz wystarczająco RFM.")
    else:
        print("Niepoprawny wybór.")

items_data.py - przykładowe przedmioty do sklepu

SHOP_ITEMS = [ {"name": "Miecz Szeptów", "price": 120}, {"name": "Zbroja Wiecznego Cienia", "price": 200}, {"name": "Mikstura Regeneracji", "price": 30}, {"name": "Runa Ognia", "price": 85}, {"name": "Pergamin Zatrucia", "price": 60}, {"name": "Zwoj Wiedźmy", "price": 150}, {"name": "Eliksir Siły", "price": 75}, {"name": "Talizman Ciernia", "price": 95}, {"name": "Zbroja Dźwiękowa", "price": 190}, {"name": "Hełm Mgielnego Kruka", "price": 110}, {"name": "Szkatułka Kruka", "price": 60}, {"name": "Złota Skrzynia", "price": 250}, ]

currencies.py (funkcje przykładowe)

def player_rfm_balance(): return 500  # przykładowo

def deduct_rfm(amount): print(f"[DEBUG] Odjęto {amount} RFM")

inventory.py (fragment interfejsu dodawania)

class Inventory: def init(self): self.items = []

def add_item(self, item):
    self.items.append(item)
    print(f"Dodano do plecaka: {item['name']}")

