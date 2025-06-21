from game_engine import GameEngine
from menu import main_menu

def main():
    print("=== FIROS: Magic & Magic ===")
    main_menu()
    engine = GameEngine()
    engine.run()

if __name__ == "__main__":
    main()
