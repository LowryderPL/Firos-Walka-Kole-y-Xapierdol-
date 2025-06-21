class MapSystem:
    def __init__(self):
        self.regions = {
            "Północne Pogranicze": "The Eldrath",
            "Wielkie Pustkowia": "Valyria Confederacy",
            "Thalijskie Wzgórza": "Empire of Thalin",
            "Zamarznięte Krainy": "K'Yoloun",
            "Mroczne Góry": "Drëbkull Fells",
            "Ziemie Cienia": "Shadoween",
            "Kraina Deszczu": "Rain",
            "Las Mistrzów": "Miswehh Thalin"
        }
        self.discovered = set()

    def display_map(self):
        print("\n=== MAPA ŚWIATA ===")
        for region, faction in self.regions.items():
            status = "✔ odkryto" if region in self.discovered else "❌ nieodkryte"
            print(f"{region} ({faction}) — {status}")

    def explore_region(self, region_name):
        if region_name in self.regions:
            self.discovered.add(region_name)
            print(f"\nOdkryto: {region_name} – teren kontrolowany przez frakcję: {self.regions[region_name]}")
        else:
            print("\nTaki region nie istnieje.")
