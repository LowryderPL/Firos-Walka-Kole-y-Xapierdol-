# main.py – Główna pętla startowa gry Firos: Magic & Magic

from menu import show_main_menu
from backpack import Backpack
from spellbook import Spellbook
from mana_system import ManaManager
from xp_system import PlayerStats
from quests import QuestLog
from alchemy import alchemy  # gotowy obiekt z recepturami

# Inicjalizacja gracza
player_name = input("🧙 Podaj imię swojego bohatera: ").strip()
if not player_name:
    player_name = "Bezimienny"

print(f"\n🎮 Witaj, {player_name}, w świecie Firos: Magic & Magic!")

# Tworzymy wszystkie systemy gracza
player_stats = PlayerStats(player_name)
player_backpack = Backpack()
player_spellbook = Spellbook()
mana = ManaManager(max_mana=50)
quest_log = QuestLog()

# Główna pętla gry
while True:
    show_main_menu(
        player_name=player_name,
        stats=player_stats,
        backpack=player_backpack,
        spellbook=player_spellbook,
        mana=mana,
        quest_log=quest_log,
        alchemy=alchemy
    )
