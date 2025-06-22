from battle_system import duel_mode, boss_fight_mode

def main():
    while True:
        print("\n=== Firos: Magic & Magic ===")
        print("1. Walka PvP (Pojedynek)")
        print("2. Walka z Bossem")
        print("3. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            duel_mode()
        elif choice == "2":
            boss_fight_mode()
        elif choice == "3":
            print("Do zobaczenia w Świecie Firos!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
