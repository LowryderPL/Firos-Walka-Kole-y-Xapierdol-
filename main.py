dfrom game_engine import GameEngine
from menu import main_menu

def main():
    print("=== FIROS: Magic & Magic ===")
    main_menu()
    engine = GameEngine()
    engine.run()

if __name__ == "__main__":
    main()
    from map_system import MapSystem

map_system = MapSystem()
map_system.display_map()
