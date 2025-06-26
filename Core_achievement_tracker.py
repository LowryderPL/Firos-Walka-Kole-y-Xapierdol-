# achievement_tracker.py — System osiągnięć FIROS

import json
from datetime import datetime

class Achievement:
    def __init__(self, id, title, description, reward_xp=0, reward_rfm=0):
        self.id = id
        self.title = title
        self.description = description
        self.reward_xp = reward_xp
        self.reward_rfm = reward_rfm

class AchievementTracker:
    def __init__(self, player_id):
        self.player_id = player_id
        self.unlocked = []
        self.filename = f"save/{player_id}_achievements.json"

    def unlock(self, achievement_id):
        if achievement_id not in self.unlocked:
            self.unlocked.append(achievement_id)
            print(f"[Osiągnięcie odblokowane] ID: {achievement_id}")

    def has_achievement(self, achievement_id):
        return achievement_id in self.unlocked

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.unlocked = data.get("unlocked", [])
        except FileNotFoundError:
            self.unlocked = []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump({
                "player_id": self.player_id,
                "unlocked": self.unlocked,
                "saved_at": datetime.utcnow().isoformat()
            }, f, indent=4)

class AchievementSystem:
    def __init__(self):
        self.achievements = self._load_achievements()

    def _load_achievements(self):
        return {
            1: Achievement(1, "Pierwsza Krew", "Wygraj swoją pierwszą bitwę", reward_xp=100, reward_rfm=5),
            2: Achievement(2, "Pogromca Potworów", "Pokonaj 10 potworów", reward_xp=200, reward_rfm=10),
            3: Achievement(3, "Uczeń Magii", "Użyj pierwszego zaklęcia", reward_xp=50),
            4: Achievement(4, "Zdobywca Ziem", "Odwiedź 5 różnych regionów", reward_xp=150),
            5: Achievement(5, "Zbieracz Artefaktów", "Zdobądź 3 unikalne artefakty", reward_xp=250, reward_rfm=20),
            6: Achievement(6, "Mistrz Rzemiosła", "Wykonaj 5 mikstur", reward_xp=120),
            7: Achievement(7, "Handlarz", "Sprzedaj przedmiot na rynku", reward_rfm=3),
            8: Achievement(8, "Bractwo Krwi", "Dołącz do Gildii", reward_xp=100),
            9: Achievement(9, "Elita PvP", "Wygraj 3 walki PvP", reward_xp=300, reward_rfm=15),
            10: Achievement(10, "Odkrywca", "Odkryj sekretne lochy", reward_xp=180)
        }

    def get_achievement(self, achievement_id):
        return self.achievements.get(achievement_id)

    def list_all(self):
        return list(self.achievements.values())

    def describe(self):
        print("📜 Lista osiągnięć:")
        for ach in self.achievements.values():
            print(f"{ach.id}. {ach.title} — {ach.description} [+{ach.reward_xp}XP, +{ach.reward_rfm} RFM]")
