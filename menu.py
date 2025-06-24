# menu.py – główne menu gry Firos: Magic & Magic (rozszerzone o alchemię, plecak i bestiariusz)

from inventory import Inventory
from faction import Faction
from map_system import map_exploration
from alchemy import alchemy_interface
from backpack import Backpack
from viev_bestiary import show_all_creatures

# Plecak globalny (dzielony z alchemią, jeśli trzeba)
player_inventory = Inventory()
player_faction = Faction("Nieprzypisany", "Brak opisu.")
player_backpack = Backpack()  # osobny widok (niezależny od alchemii, ale można połączyć)

def main_menu():
    while True:
        print("\n=== GŁÓWNE MENU FIROS: MAGIC & MAGIC ===")
        print("1. 🌍 Eksploracja mapy")
        print("2. 🎒 Plecak (scrolls, składniki, artefakty)")
        print("3. ⚗️ Alchemia (stół alchemiczny)")
        print("4. 📚 Bestiariusz")
        print("5. 🏹 Frakcja")
        print("6. ❌ Wyjście z gry")

        choice = input("Wybierz opcję (1-6): ").strip()

        if choice == "1":
            map_exploration()
        elif choice == "2":
            player_backpack.show()
        elif choice == "3":
            alchemy_interface()
        elif choice == "4":
            show_all_creatures()
        elif choice == "5":
            print("\n--- Informacje o frakcji ---")
            print(player_faction)
        elif choice == "6":
            print("👋 Do zobaczenia w Świecie Firos!")
            break
        else:
            print("❌ Nieprawidłowy wybór.")

# Uruchomienie głównego menu
if __name__ == "__main__":
    main_menu()
