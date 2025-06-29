import sqlite3

class Item:
    def __init__(self, name, weight, type_):
        self.name = name
        self.weight = weight
        self.type_ = type_

    def __str__(self):
        return f"{self.name} ({self.type_}, {self.weight} kg)"


class NFTItem:
    def __init__(self, name, rarity, power, bonus_effect):
        self.name = name
        self.rarity = rarity
        self.power = power
        self.bonus_effect = bonus_effect

    def __str__(self):
        return f"[{self.rarity}] {self.name} – Moc: {self.power} | Efekt: {self.bonus_effect}"


class Inventory:
    def __init__(self, max_weight=50):
        self.items = []
        self.max_weight = max_weight

    def current_weight(self):
        return sum(item.weight for item in self.items)

    def add_item(self, item):
        if self.current_weight() + item.weight <= self.max_weight:
            self.items.append(item)
            print(f"✅ Dodano: {item}")
        else:
            print("❌ Przekroczono limit wagi!")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"🗑️ Usunięto: {item}")
                return
        print("❌ Przedmiot nie znaleziony.")

    def show_inventory(self):
        print("=== 🎒 Ekwipunek ===")
        for item in self.items:
            print(item)
        print(f"🔸 Obciążenie: {self.current_weight()}/{self.max_weight} kg")

    def filter_inventory(self, type_):
        print(f"=== 📦 Filtr: {type_} ===")
        for item in self.items:
            if item.type_ == type_:
                print(item)


def pokaz_nft_w_ekwipunku(db_path="firos_game_database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name, rarity, power, bonus_effect FROM nft_inventory")
        nft_items = cursor.fetchall()
    except sqlite3.OperationalError:
        print("⚠️ Tabela NFT nie istnieje.")
        conn.close()
        return

    conn.close()

    if nft_items:
        print("\n=== 🎴 Twoje NFT ===")
        for nft in nft_items:
            print(NFTItem(*nft))
    else:
        print("\nBrak NFT w ekwipunku.")


# 🔄 Przykład użycia
if __name__ == "__main__":
    inv = Inventory()
    inv.add_item(Item("Zbroja Wilka", 7, "Zbroja"))
    inv.add_item(Item("Miecz Cienia", 4, "Broń"))
    inv.show_inventory()
    pokaz_nft_w_ekwipunku()
