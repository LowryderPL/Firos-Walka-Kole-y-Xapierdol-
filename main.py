from game_engine import GameEngine
from menu import main_menu
from map_system import MapSystem
from faction import choose_faction

def main():
    print("=== FIROS: Magic & Magic ===")
    main_menu()

    # wybór frakcji
    faction = choose_faction()
    if faction is None:
        return

    # uruchomienie gry
    engine = GameEngine()
    engine.run()

    # wyświetlenie mapy
    map_system = MapSystem()
    map_system.display_map()

if __name__ == "__main__":
    main()
