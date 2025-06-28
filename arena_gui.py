# arena_gui.py

import time
import sys
import random
from arena import ArenaBattle, ARENA_TYPES, SPECIAL_ARENAS, TOURNAMENT_ARENAS
from ui_elements import print_with_border, pause, clear_screen
from player_profile import load_player_profile
from core_save_load import save_game_state
from core_ranking import display_ranking, display_faction_ranking, display_season_rewards
from narrator import random_battle_quote

def slow_type(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_loading(text="Ładowanie Areny"):
    for i in range(3):
        sys.stdout.write(f"\r{text}{'.' * (i + 1)}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def display_arena_menu(player):
    clear_screen()
    print_with_border("🛡️ FIROS: ARENA BITEW 🛡️")
    print("\nWybierz typ Areny:\n")
    for idx, arena_type in enumerate(ARENA_TYPES):
        print(f" {idx + 1}. {arena_type}")
    print("\n--- ARENY SPECJALNE ---")
    for idx, arena_type in enumerate(SPECIAL_ARENAS):
        print(f" S{idx + 1}. {arena_type}")
    print("\n--- ARENY TURNIEJOWE ---")
    for idx, arena_type in enumerate(TOURNAMENT_ARENAS):
        print(f" T{idx + 1}. {arena_type}")
    print("\n 0. Powrót")

    choice = input("\nTwój wybór: ").strip().upper()

    if choice == "0":
        return
    elif choice.startswith("S"):
        index = int(choice[1:]) - 1
        selected_type = SPECIAL_ARENAS[index]
    elif choice.startswith("T"):
        index = int(choice[1:]) - 1
        selected_type = TOURNAMENT_ARENAS[index]
    else:
        try:
            index = int(choice) - 1
            selected_type = ARENA_TYPES[index]
        except:
            print("❌ Nieprawidłowy wybór.")
            pause(1.5)
            return display_arena_menu(player)

    handle_arena_battle(player, selected_type)

def handle_arena_battle(player, arena_type):
    clear_screen()
    quote = random_battle_quote()
    print_with_border(f"⚔️  WALKA NA ARENIE: {arena_type} ⚔️")
    slow_type(f"„{quote}”", delay=0.04)
    animated_loading("Przywoływanie przeciwnika")

    arena = ArenaBattle(player, arena_type=arena_type, is_ranked=True)
    logs = arena.start_battle()

    for line in logs:
        slow_type(f" > {line}", delay=random.uniform(0.02, 0.06))
        time.sleep(0.3)

    print("\n🔥 WALKA ZAKOŃCZONA 🔥")
    slow_type("🎁 Przydzielanie nagród...")
    save_game_state(player)
    pause(2)
    post_arena_menu(player)

def post_arena_menu(player):
    print_with_border("🏆 MENU ARENY")
    print(" 1. Pokaż ranking ogólny")
    print(" 2. Ranking frakcji")
    print(" 3. Nagrody sezonowe")
    print(" 4. Wróć do wyboru Areny")
    print(" 0. Powrót do gry")

    choice = input("Twój wybór: ").strip()
    if choice == "1":
        display_ranking()
    elif choice == "2":
        display_faction_ranking()
    elif choice == "3":
        display_season_rewards()
    elif choice == "4":
        display_arena_menu(player)
    else:
        slow_type("🔙 Powrót do głównego świata gry...")

# Test lokalny
if __name__ == "__main__":
    player = load_player_profile("default_player")
    display_arena_menu(player)
