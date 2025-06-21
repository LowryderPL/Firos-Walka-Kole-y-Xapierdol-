class MapSystem:
    def __init__(self):
        self.regions = {
            "Północne Pogranicze": "The Eldrath",
            "Wielkie Pustkowia": "Valyria Confederacy",
            "Thaliijskie Wzgórza": "Empire of Thalin",
            "Zamarznięte Krainy": "K'Yoloun",
            "Góry Orków": "Drekbull Kells",
            "Ziemie Cienia": "Shadoween",
            "Kraina Deszczu": "Rain",
            "Lasy Mgieł": "Miswevh Thalin"
        }
        self.discovered = set()

    def display_map(self):
        print("\n=== MAPA ŚWIATA ===")
        for region
