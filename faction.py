def choose_faction():
    print("=== WYBIERZ FRAKCJĘ ===")
    print("1. The Eldrath")
    print("2. Yalyria Confederacy")
    print("3. Empire of Thalin")

    choice = input("Wybierz frakcję (1-3): ").strip()
    
    factions = {
        "1": "The Eldrath",
        "2": "Yalyria Confederacy",
        "3": "Empire of Thalin"
    }

    faction = factions.get(choice, "Nieznana frakcja")
    print(f"Wybrałeś: {faction}")
    return faction
