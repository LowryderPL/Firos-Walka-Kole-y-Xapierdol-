class Faction:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"=== Frakcja: {self.name} ===")
        print(self.description)


def get_factions():
    return [
        Faction("The Eldrath", "Dawni magowie północy, władający starożytną magią i tajemnymi rytuałami."),
        Faction("Valyria Confederacy", "Zjednoczenie wolnych miast pustyni – szybkie jednostki, złoto i kupcy."),
        Faction("Empire of Thalin", "Imperium ludzi – duma, potęga i rycerski porządek."),
        Faction("Kyloun", "Zimna, surowa kraina pamięci, pełna wojowników lodu."),
        Faction("Drekkul Fells", "Mroczne góry zamieszkane przez nekromantów i zbiegów."),
        Faction("Shadoween", "Ukryta frakcja skrytobójców, mistrzów cienia."),
        Faction("Rain", "Magowie burz i deszczu, panujący nad pogodą."),
        Faction("Misweth Thalin", "Elfy lasu, strzegące tajemnic pradawnych drzew.")
    ]


def choose_faction():
    factions = get_factions()

    print("=== WYBIERZ SWOJĄ FRAKCJĘ ===")
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
