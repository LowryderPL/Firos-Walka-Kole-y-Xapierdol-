from game_engine import GameEngine
from menu import main_menu
from map_system import MapSystem

def main():
    print("=== FIROS: Magic & Magic ===")
    main_menu()
    
    engine = GameEngine()
    engine.run()

    map_system = MapSystem()
    map_system.display_map()

if __name__ == "__main__":
    main()
