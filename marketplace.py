# marketplace.py — Firos: Magic & Magic
# Pełny system handlu: przedmioty, karty NFT, waluty RFN/TON

class Item:
    def __init__(self, name, description, rarity, price_rfn, price_ton):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.price_rfn = price_rfn
        self.price_ton = price_ton

class Marketplace:
    def __init__(self):
        self.items = []  # lista przedmiotów dostępnych
        self.transactions = []  # historia transakcji

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [i for i in self.items if i.name != item_name]

    def list_items(self):
        return [{
            "name": item.name,
            "rarity": item.rarity,
            "RFN": item.price_rfn,
            "TON": item.price_ton
        } for item in self.items]

    def buy_item(self, item_name, buyer, currency):
        for item in self.items:
            if item.name == item_name:
                if currency == "RFN" and buyer.rfn >= item.price_rfn:
                    buyer.rfn -= item.price_rfn
                    self.transactions.append((buyer.name, item_name, "RFN"))
                    return f"{buyer.name} kupił {item.name} za {item.price_rfn} RFN"
                elif currency == "TON" and buyer.ton >= item.price_ton:
                    buyer.ton -= item.price_ton
                    self.transactions.append((buyer.name, item_name, "TON"))
                    return f"{buyer.name} kupił {item.name} za {item.price_ton} TON"
                else:
                    return "Nie masz wystarczających środków!"
        return "Przedmiot nie istnieje!"

# Przykładowy użytkownik
class Player:
    def __init__(self, name, rfn, ton):
        self.name = name
        self.rfn = rfn
        self.ton = ton

# Przykład działania
if __name__ == "__main__":
    marketplace = Marketplace()
    sword = Item("Miecz Runiczny", "Starożytny miecz o mocy ognia", "epicki", 200, 0.5)
    nft_card = Item("Karta Bohatera: Żarogniew", "Unikalna karta NFT", "legendarna", 0, 1.2)

    marketplace.add_item(sword)
    marketplace.add_item(nft_card)

    gracz = Player("Wiedźmograd", 500, 2.0)
    print(marketplace.buy_item("Miecz Runiczny", gracz, "RFN"))
    print(marketplace.buy_item("Karta Bohatera: Żarogniew", gracz, "TON"))
