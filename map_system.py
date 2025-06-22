class Faction:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"\n=== Frakcja: {self.name} ===")
        print(self.description)

def get_factions():
    return [
        Faction("The Eldrath", "Dawni magowie północy, władający starożytną magią."),
        Faction("Valyria Confederacy", "Zjednoczenie wolnych miast pustyni – mistrzowie alchemii."),
        Faction("Empire of Thalin", "Imperium ludzi – duma, potęga i rycerski honor."),
        Faction("K’Yoloun", "Zimna, surowa kraina pamięci, pełna wojowników lodu."),
        Faction("Drekbull Fells", "Wrogoce góry zamieszkałe przez nekromantów."),
        Faction("Shadowen", "Ukryta frakcja skrytobójców, mistrzów cienia."),
        Faction("Rain", "Magowie burz i deszczu, panujący nad pogodą."),
        Faction("Miswehh Thalin", "Elfy lasu, strzegące tajemnic pradawnych cywilizacji.")
    ]

def choose_faction():
    factions = get_factions()
    print("\n=== WYBIERZ SWOJĄ FRAKCJĘ ===")
    for idx, faction in enumerate(factions, start=1):
        print(f"{idx}. {faction.name}")
    
    choice = input("Wybierz numer frakcji: ").strip()
    try:
        selected = factions[int(choice) - 1]
        selected.display_info()
        return selected
    except (IndexError, ValueError):
        print("Nieprawidłowy wybór.")
        return None
