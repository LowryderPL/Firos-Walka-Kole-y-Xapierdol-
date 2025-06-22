class Location:
    def __init__(self, name, description, connected_locations=None):
        self.name = name
        self.description = description
        self.connected_locations = connected_locations if connected_locations else []

    def display(self):
        print(f"\n=== {self.name.upper()} ===")
        print(self.description)
        print("Możesz iść do:")
        for idx, loc in enumerate(self.connected_locations, start=1):
            print(f"{idx}. {loc.name}")

class MapSystem:
    def __init__(self):
        self.current_location = None

    def set_starting_location(self, location):
        self.current_location = location

    def travel(self):
        if not self.current_location:
            print("Nie ustawiono lokalizacji początkowej.")
            return

        self.current_location.display()
        try:
            choice = int(input("Wybierz numer lokacji, do której chcesz się udać: ")) - 1
            if 0 <= choice < len(self.current_location.connected_locations):
                self.current_location = self.current_location.connected_locations[choice]
                print(f"\n➡️ Przeniesiono do: {self.current_location.name}")
            else:
                print("Nieprawidłowy wybór.")
        except ValueError:
            print("Musisz podać liczbę.")

# === Lokacje świata gry ===
village = Location("Wioska Startowa", "Mała osada otoczona lasami i łąkami.")
forest = Location("Mroczny Las", "Gęsty, ciemny las pełen dzikich stworzeń.")
mountains = Location("Zamarznięte Szczyty", "Lodowe góry na północy, niedostępne i zdradliwe.")

# Połączenia
village.connected_locations = [forest, mountains]
forest.connected_locations = [village]
mountains.connected_locations = [village]

# Instancja mapy
game_map = MapSystem()
game_map.set_starting_location(village)

# Funkcja do uruchomienia eksploracji
def map_exploration():
    print("\n=== TRYB EKSPLORACJI ===")
    while True:
        game_map.travel()
        cont = input("Czy chcesz kontynuować eksplorację? (t/n): ").strip().lower()
        if cont != "t":
            break
