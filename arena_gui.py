# arena_gui.py

from arena import ArenaBattle, ARENA_TYPES
from ui_elements import print_with_border, pause
from player_profile import load_player_profile
from core_ranking import display_ranking
from core_save_load import save_game_state

def display_arena_menu(player):
    print_with_border("=== ARENA BITEW ===")
    print("Wybierz typ Areny:\n")
    for idx, arena_type in enumerate(ARENA_TYPES):
        print(f"{idx + 1}. {arena_type}")
    print("0. Powrót")

    choice = input("\nTwój wybór: ").strip()
    if choice == "0":
        return

    try:
        choice_index = int(choice) - 1
        if choice_index not in range(len(ARENA_TYPES)):
            raise ValueError
        selected_type = ARENA_TYPES[choice_index]
        handle_arena_battle(player, selected_type)
    except ValueError:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        display_arena_menu(player)

def handle_arena_battle(player, arena_type):
    print_with_border(f"⛨ Rozpoczynasz walkę na Arenie: {arena_type}")
    arena = ArenaBattle(player, arena_type=arena_type, is_ranked=True)
    logs = arena.start_battle()

    for line in logs:
        print(line)
        pause(0.5)

    print("\nWalka zakończona!")
    print_with_border("Nagrody i doświadczenie zostały przydzielone.")
    save_game_state(player)
    pause(2)

    post_arena_menu(player)

def post_arena_menu(player):
    print("\nCo dalej?")
    print("1. Pokaż ranking")
    print("2. Wróć do Areny")
    print("0. Wyjdź")

    choice = input("Twój wybór: ").strip()
    if choice == "1":
        display_ranking()
        post_arena_menu(player)
    elif choice == "2":
        display_arena_menu(player)
    else:
        print("Powrót do gry...")

# Optional test run
if __name__ == "__main__":
    player = load_player_profile("default_player")
    display_arena_menu(player)
