class Map:
    def __init__(self):
        self.current_region = "Początkowa Kraina"
        self.regions = {
            "Początkowa Kraina": {"frakcja": "Neutralna", "odkryta": True},
            "Ruiny Cienia": {"frakcja": "Cienie", "odkryta": False},
            "Ziemie Krwi": {"frakcja": "Krwawe Ostrza", "odkryta": False},
            "Wieczna Zmarzlina": {"frakcja": "Lodowi Jeźdźcy", "odkryta": False},
            "Twierdza Magów": {"frakcja": "Zakon Wiedzy", "odkryta": False}
        }

    def display_starting_area(self):
        print(f"\n🗺️ Rozpoczynasz w: {self.current_region}")
        self.show_current_region()

    def show_current_region(self):
        print(f"\n📍 Region: {self.current_region}")
        info = self.regions[self.current_region]
        print(f"⚔️ Kontrola frakcji: {info['frakcja']}")
        print(f"👁️ Odkryty: {'Tak' if info['odkryta'] else 'Nie'}")

    def show(self):
        print("\n🌍 Mapa Świata FIROS:")
        for region, info in self.regions.items():
            odkryta = "✅" if info["odkryta"] else "❌"
            print(f" - {region} [{info['frakcja']}] - {odkryta}")
