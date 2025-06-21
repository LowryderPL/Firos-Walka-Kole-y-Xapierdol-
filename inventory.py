inventory = {
    "Miecz Początkującego": 1,
    "Zbroja Skórzana": 1,
    "Mikstura Leczenia": 3
}

def show_inventory():
    print("\n=== EKWIPUNEK ===")
    if not inventory:
        print("Twój ekwipunek jest pusty.")
        return
    for item, quantity in inventory.items():
        print(f"{item} x{quantity}")
