# exploration.py – Eksploracja świata, składniki, potwory i wydarzenia

import random
from backpack import Backpack
from viev_bestiary import show_all_creatures  # lub system encounterów
from xp_system import PlayerStats

# Lista lokacji do eksploracji
locations = [
    {
        "name": "Mroczny Las",
        "description": "Ciemny las pełen ziół, ale też niebezpiecznych stworzeń.",
        "loot": ["ziele", "grzyb", "popiół", "krew"],
        "enemy_chance": 30,
        "event": "szept w krzakach"
    },
    {
        "name": "Bagna Cienia",
        "description": "Zarośnięte bagno pełne pułapek i zmutowanych owadów.",
        "loot": ["cień", "woda", "jadowity mech"],
        "enemy_chance": 40,
        "event": "znalazłeś porzucone ciało"
    },
    {
        "name": "Ruiny Starożytnych",
        "description": "Ruiny miasta sprzed tysiącleci. Może coś tu zostało?",
        "loot": ["runiczny_papier", "pergamin", "kamień rytualny"],
        "enemy_chance": 50,
        "event": "głuchy dźwięk w oddali"
    }
]

# Globalne obiekty
player_backpack = Backpack()
player_stats = PlayerStats("Gracz")

def explore():
    print("\n🌍 Wybierz lokację do eksploracji:")
    for idx, loc in enumerate(locations, 1):
        print(f"{idx}. {loc['name']} – {loc['description']}")

    choice = input("Wybierz numer lokacji: ").strip()
    if not choice.isdigit():
        print("❌ Nieprawidłowy wybór.")
        return

    idx = int(choice) - 1
    if not (0 <= idx < len(locations)):
        print("❌ Nieprawidłowy numer.")
        return

    loc = locations[idx]
    print(f"\n🧭 Eksplorujesz: {loc['name']}...")
    print(f"🌫️ {loc['event']}")

    # Szansa na walkę z potworem
    if random.randint(1, 100) <= loc["enemy_chance"]:
        print("⚔️ Zostałeś zaatakowany przez potwora!")
        show_all_creatures()  # można tu podpiąć walkę
        player_stats.gain_exp(75)  # testowy drop EXP
    else:
        print("🤫 Cicho i spokojnie...")

    # Szansa na loot
    loot_found = random.sample(loc["loot"], k=random.randint(1, min(3, len(loc["loot"]))))
    for item in loot_found:
        player_backpack.add_ingredient(item)

    player_stats.show_exp()

# Test samodzielny
if __name__ == "__main__":
    while True:
        explore()
        again = input("\nEksplorować dalej? (t/n): ").strip().lower()
        if again != "t":
            break
