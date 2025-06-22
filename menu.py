from inventory import Inventory
from faction import Faction
from map_system import map_exploration

def main_menu():
    inventory = Inventory()
    faction = Faction("Nieprzypisany", "Brak opisu.")  # Można nadpisać później wyborem gracza

    while True:
        print("\n=== GŁÓWNE MENU FIROS: MAGIC & MAGIC ===")
        print("1. Rozpocznij eksplorację")
        print("2. Pokaż ekwipunek")
        print("3. Informacje o frakcji")
        print("4. Wyjście z gry")

        choice = input("Wybierz opcję (1-4): ").strip()

        if choice == "1":
            map_exploration()
        elif choice == "2":
            inventory.display()
        elif choice == "3":
            print("\n--- Informacje o Twojej frakcji ---")
            print(faction)
        elif choice == "4":
            print("Zamykanie gry... Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
