inventory = {
    "Złoto": 150,
    "Mikstura leczenia": 3,
    "Zwoje teleportacji": 1,
    "Stalowy miecz": 1,
    "Fragment mapy": 0
}

def show_inventory():
    print("\n=== TWÓJ EKWIPUNEK ===")
    if not inventory:
        print("Ekwipunek jest pusty.")
    else:
        for item, amount in inventory.items():
            print(f"{item}: {amount} szt.")
