class FactionManager:
    def __init__(self):
        self.factions = {
            "Cienie": {
                "bonus": "+10% obrażeń nocą",
                "talenty": ["Skrytobójstwo", "Iluzje", "Cisza"],
            },
            "Krwawe Ostrza": {
                "bonus": "+20% obrażeń przy <50% HP",
                "talenty": ["Szał", "Zemsta", "Wściekłość"],
            },
            "Lodowi Jeźdźcy": {
                "bonus": "Zamrażają przeciwników na 1 turę co 5 ataków",
                "talenty": ["Lodowy Mur", "Frostbite", "Spowolnienie"],
            },
            "Zakon Wiedzy": {
                "bonus": "+15% moc czarów",
                "talenty": ["Płonący Pocisk", "Bariery", "Teleportacja"],
            },
        }
        self.player_faction = None

    def choose_faction(self):
        print("\n🏰 Wybierz frakcję:")
        for idx, (name, data) in enumerate(self.factions.items(), 1):
            print(f"{idx}. {name} - {data['bonus']}")
        choice = input(">> ")
        keys = list(self.factions.keys())
        try:
            self.player_faction = keys[int(choice) - 1]
            print(f"\n✅ Wybrano frakcję: {self.player_faction}")
        except (IndexError, ValueError):
            print("❌ Nieprawidłowy wybór.")
            self.choose_faction()

    def get_faction_bonus(self):
        return self.factions[self.player_faction]["bonus"] if self.player_faction else None

    def get_faction_talents(self):
        return self.factions[self.player_faction]["talenty"] if self.player_faction else []
