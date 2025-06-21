def main_menu():
    while True:
        print("\n=== MENU GŁÓWNE ===")
        print("1. Rozpocznij grę")
        print("2. Wyświetl ekwipunek")
        print("3. Pokaż mapę")
        print("4. Wybierz frakcję")
        print("5. Wyjście")

        choice = input("Wybierz opcję (1-5): ").strip()

        if choice == "1":
            print(">> Rozpoczynasz przygodę w świecie Firos...")
            break  # Wyjście z menu, gra startuje
        elif choice == "2":
            from inventory import show_inventory
            show_inventory()
        elif choice == "3":
            from map_system import MapSystem
            map_system = MapSystem()
            map_system.display_map()
        elif choice == "4":
            from faction import choose_faction
            choose_faction()
        elif choice == "5":
            print(">> Do zobaczenia, bohaterze!")
            exit()
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
