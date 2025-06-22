from game_engine import GameEngine
from map_system import Map
from faction import FactionManager
from inventory import Inventory
from quests import QuestLog
from bestiary import Bestiary
from sqlite_db import DBHandler

def start_game():
    print("🎮 Witaj w świecie Firos: Magic & Magic!")
    engine = GameEngine()
    engine.run()

if __name__ == "__main__":
    start_game()
