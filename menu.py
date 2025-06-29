import sys
from inventory import show_inventory, pokaz_nft_w_ekwipunku
from quests import start_quest, list_quests
from spellbook import list_spells
from rituals import list_rituals
from map_system import show_map
from alchemy import show_alchemy_options
from game_engine import start_game
from marketplace_logic import show_marketplace

def display_menu():
    print("""
====================================
     🔮 FIROS: MAGIC & MAGIC 🔮
====================================
 1. Rozpocznij grę
 2. Mapa świata
 3. Ekwipunek
 4. Karty NFT
 5. Questy i Misje
 6. Księga zaklęć
 7. Rytuały i zaklęcia
 8. Alchemia i crafting
 9. Marketplace NFT / RFN
10. Wyjście z gry
====================================
""")

def handle_choice(choice):
    if choice == "1":
        start_game()
    elif choice == "2":
        show_map()
    elif choice == "3":
        show_inventory()
    elif choice == "4":
        pokaz_nft_w_ekwipunku()
    elif choice == "5":
        list_quests()
    elif choice == "6":
        list_spells()
    elif choice == "7":
        list_rituals()
    elif choice == "8":
        show_alchemy_options()
    elif choice == "9":
        show_marketplace()
    elif choice == "10":
        print("Do zobaczenia w świecie FIROS...")
        sys.exit()
    else:
        print("Nieprawidłowy wybór. Wybierz ponownie.")

def main():
    while True:
        display_menu()
        choice = input("Wybierz opcję: ")
        handle_choice(choice)

if __name__ == "__main__":
    main()
