class Creature:
    def __init__(self, name, hp, damage, loot, rarity, description):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.loot = loot
        self.rarity = rarity
        self.description = description

    def show_info(self):
        print(f"\n🗡️ {self.name} [{self.rarity}]")
        print(f"HP: {self.hp} | Obrażenia: {self.damage}")
        print(f"Opis: {self.description}")
        print(f"Drop: {', '.join(self.loot)}")

def get_bestiary():
    return [
        Creature("Wilk z Cienia", 80, 12, ["Skóra Wilka", "Ząb Cienia"], "Zwykły", "Dziki i szybki, unika światła."),
        Creature("Topielec", 120, 15, ["Oślizgłe Błoto", "Ząb"], "Rzadki", "Bestia z bagien, wyciąga żywych pod wodę."),
        Creature("Upiorna Wiedźma", 160, 25, ["Zioła Rytualne", "Runa Krwi"], "Epicki", "Szepcze do umysłów wojowników."),
        Creature("Strażnik Krypty", 200, 30, ["Kość Bohatera", "Klejnot Cienia"], "Unikalny", "Nieumarły rycerz, broni starożytnego grobowca."),
        Creature("Władca Smoków", 500, 60, ["Serce Smoka", "Korona Popiołów", "Artefakt Ognia"], "Legendarny", "Potężny smok, kontrolujący żywioł ognia."),
    ]

def show_bestiary():
    bestiary = get_bestiary()
    print("\n=== Bestiariusz Świata Firos ===")
    for idx, monster in enumerate(bestiary, 1):
        print(f"{idx}. {monster.name} ({monster.rarity})")
    choice = input("Wybierz numer, aby zobaczyć szczegóły: ").strip()
    try:
        bestiary[int(choice)-1].show_info()
    except:
        print("Nieprawidłowy wybór.")
