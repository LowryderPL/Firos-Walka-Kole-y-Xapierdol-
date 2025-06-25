main.py – uproszczony widok do telefonu

def wybierz_klase(): klasy = { "1": "Żarowid", "2": "Krwiścier", "3": "Wiedźcior", "4": "Mrokorzyt", "5": "Stryłecznik", "6": "Zielarzec", "7": "Snemistrz" }

print("Wybierz swoją klasę postaci:")
for klucz, nazwa in klasy.items():
    linia = klucz + ". " + nazwa
    print(linia)

wybor = input("Podaj numer klasy: ")
wybrana = klasy.get(wybor, "Wiedźcior")

print("\nTwoja postać to: ")
print(wybrana)
return wybrana

def start_gry(): print("\nWitaj w świecie FIROS!") imie = input("Podaj imię swojej postaci: ") klasa = wybierz_klase()

postac = {
    "nazwa": imie,
    "klasa": klasa,
    "poziom": 1,
    "punkty_zdrowia": 100,
    "mana": 50,
    "ekwipunek": [],
    "czary": []
}

print("\nGotowy do przygody:")
print(postac["nazwa"] + " – " + postac["klasa"])

return postac

if name == "main": gracz = start_gry() # tu kontynuacja: menu, walka, mapa itd.

