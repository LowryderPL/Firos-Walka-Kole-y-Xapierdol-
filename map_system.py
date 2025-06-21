
class MapSystem:
    def __init__(self):
        self.regions = [
            "Kyloun",
            "Drekkul Fells",
            "Shadoween",
            "Rain",
            "Misweth Thalin",
            "Empire of Thalin"
        ]

    def display_map(self):
        print("=== MAPA ŚWIATA ===")
        for i, region in enumerate(self.regions, 1):
            print(f"{i}. {region}")
