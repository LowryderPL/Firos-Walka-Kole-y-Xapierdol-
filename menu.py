# menu.py – Główne menu gry Firos: Magic & Magic

from battle_system import start_battle
from exploration import explore
from dungeon import enter_dungeon
from spellbook import show_spells
from quests import show_quests
from backpack import show_backpack
from alchemy import show_alchemy_menu

def show_main_menu(player_name, stats, backpack, spellbook, mana, quest_log, alchemy):
    while True:
        print(f"\n🎮 {player_name}, wybierz jedną z opcji:")
        print("1. ⚔️  Walka z potworem")
        print("2. 🌲 Eksploracja świata")
        print("3. 📜 Księga Zaklęć")
        print("4. 🧪 Alchemia i mikstury")
        print("5. 🎒 Plecak i składniki")
        print("6. 🧠 Statystyki i EXP")
        print("7. 📖 Dziennik misji")
        print("8. 💧 Zarządzanie maną")
        print("9. 💀 Wejście do lochu")
        print("0. ❌ Wyjście z gry")

        choice = input("➤ Twój wybór: ").strip()

        if choice == "1":
            start_battle(stats, backpack)
        elif choice == "2":
            explore()
        elif choice == "3":
            show_spells(spellbook, mana)
        elif choice == "4":
            show_alchemy_menu(alchemy, backpack)
        elif choice == "5":
            show_backpack(backpack)
        elif choice == "6":
            stats.show_stats()
        elif choice == "7":
            show_quests(quest_log)
        elif choice == "8":
            print(f"\n🔮 Aktualna mana: {mana.current}/{mana.max}")
        elif choice == "9":
            enter_dungeon()
        elif choice == "0":
            print("👋 Zakończono grę. Do zobaczenia!")
            break
        else:
            print("❗ Nieprawidłowy wybór. Spróbuj ponownie.")
