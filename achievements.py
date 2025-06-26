import datetime

class Achievement: def init(self, code, name, description, reward, condition_func): self.code = code  # unikalny identyfikator self.name = name self.description = description self.reward = reward  # np. XP, RFM, Tytuł self.condition_func = condition_func  # funkcja sprawdzająca, czy zdobyte

class AchievementTracker: def init(self): self.achievements = [] self.unlocked = set()

def add_achievement(self, achievement):
    self.achievements.append(achievement)

def check_all(self, player):
    unlocked_now = []
    for a in self.achievements:
        if a.code not in self.unlocked and a.condition_func(player):
            self.unlocked.add(a.code)
            unlocked_now.append((a.name, a.reward))
    return unlocked_now

def list_achievements(self):
    return [(a.name, a.description, a.code in self.unlocked) for a in self.achievements]

---------------------- PRZYKŁADOWE WARUNKI ----------------------

def defeated_enemies(min_count): return lambda p: p.total_enemies_defeated >= min_count

def completed_quests(min_count): return lambda p: p.total_quests_completed >= min_count

def explored_places(min_count): return lambda p: len(p.explored_locations) >= min_count

def collected_items(min_count): return lambda p: len(p.inventory) >= min_count

def joined_guild(): return lambda p: p.guild is not None

def time_played(hours): return lambda p: p.play_time >= datetime.timedelta(hours=hours)

def secret_title(name): return lambda p: name in p.titles

---------------------- DEFINICJA OSIĄGNIĘĆ ----------------------

def generate_default_achievements(): return [ Achievement("first_blood", "Pierwsza krew", "Pokonaj pierwszego przeciwnika", {"XP": 100}, defeated_enemies(1)), Achievement("slayer10", "Pogromca", "Pokonaj 10 przeciwników", {"XP": 250, "RFM": 10}, defeated_enemies(10)), Achievement("slayer100", "Rzeźnik", "Pokonaj 100 przeciwników", {"XP": 1000, "RFM": 100}, defeated_enemies(100)),

Achievement("adventurer1", "Pierwszy krok", "Wykonaj pierwszą misję", {"XP": 150}, completed_quests(1)),
    Achievement("hero25", "Bohater", "Ukończ 25 misji", {"XP": 750, "RFM": 20}, completed_quests(25)),
    Achievement("legend", "Legenda", "Ukończ 100 misji", {"XP": 2500, "RFM": 200, "Tytuł": "Legenda Firos"}, completed_quests(100)),

    Achievement("wanderer", "Wędrowiec", "Odkryj 5 lokacji", {"XP": 200}, explored_places(5)),
    Achievement("cartographer", "Kartograf", "Odkryj 20 lokacji", {"XP": 500, "RFM": 25}, explored_places(20)),

    Achievement("collector", "Zbieracz", "Zbierz 10 przedmiotów", {"XP": 200}, collected_items(10)),
    Achievement("hoarder", "Kolekcjoner", "Zbierz 50 przedmiotów", {"XP": 800, "RFM": 30}, collected_items(50)),

    Achievement("guild_joined", "Bractwo", "Dołącz do gildii", {"XP": 100, "Tytuł": "Gildyjny Adept"}, joined_guild()),
    Achievement("guild_master", "Mistrz Gildii", "Zostań liderem gildii", {"XP": 2000, "RFM": 150}, lambda p: p.guild_role == "leader"),

    Achievement("playtime1", "Zatracenie", "Spędź 1 godzinę w grze", {"XP": 100}, time_played(1)),
    Achievement("playtime20", "Weteran", "Spędź 20 godzin w grze", {"XP": 1500, "RFM": 40}, time_played(20)),

    Achievement("secret_shadow", "Sekret: Cień", "Zdobądź tytuł \"Mistrz Cienia\"", {"Tytuł": "Czarny Rytuał", "XP": 1000}, secret_title("Mistrz Cienia")),
    Achievement("secret_glory", "Sekret: Chwała", "Zdobądź tytuł \"Bohater Chwały\"", {"XP": 1500, "RFM": 60}, secret_title("Bohater Chwały")),

    # PvP, Boss, Alchemia
    Achievement("duelist", "Pojedynek", "Wygraj pierwszy pojedynek PvP", {"XP": 300}, lambda p: p.pvp_wins >= 1),
    Achievement("champion10", "Czempion", "Wygraj 10 pojedynków PvP", {"XP": 1200, "RFM": 40}, lambda p: p.pvp_wins >= 10),

    Achievement("boss_slayer", "Pogromca Bossów", "Pokonaj 1 bossa", {"XP": 500, "Artefakt": "Losowy"}, lambda p: p.bosses_defeated >= 1),
    Achievement("boss_king", "Król Pogromców", "Pokonaj 10 bossów", {"XP": 3000, "TON": 1}, lambda p: p.bosses_defeated >= 10),

    Achievement("alchemy_init", "Alchemiczna Przygoda", "Utwórz pierwszą miksturę", {"XP": 150}, lambda p: p.potions_created >= 1),
    Achievement("alchemy_master", "Mistrz Eliksirów", "Stwórz 50 mikstur", {"XP": 2000, "RFM": 100}, lambda p: p.potions_created >= 50),

    Achievement("scrolls_user", "Zwojowy Uczeń", "Użyj pierwszego zwoju", {"XP": 120}, lambda p: p.scrolls_used >= 1),
    Achievement("rune_archiv

