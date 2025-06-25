spells_data.py – pełny system czarów z GUI dla 7 klas, zamknięty i gotowy do użycia

spell_data = { "Żarowid": [ {"name": "Iskra Zarwena", "description": "Wystrzeliwuje iskrę ognia wprost w przeciwnika.", "mana_cost": 10, "power": 25, "level": 1, "type": "active"}, {"name": "Płomień Kłusaka", "description": "Podpala pole bitwy, raniąc wrogów przez 3 tury.", "mana_cost": 15, "power": 35, "level": 2, "type": "active"}, {"name": "Bariera Żaru", "description": "Magiczna bariera zmniejszająca obrażenia.", "mana_cost": 12, "power": 0, "level": 2, "type": "buff"}, {"name": "Runiczny Ogień", "description": "Runy na ziemi eksplodują przy zbliżeniu się wroga.", "mana_cost": 18, "power": 30, "level": 3, "type": "active"}, {"name": "Krąg Gorąca", "description": "Aura żaru zadaje obrażenia wszystkim pobliskim celom.", "mana_cost": 22, "power": 40, "level": 4, "type": "active"}, {"name": "Oczyszczenie Płomieniem", "description": "Usuwa negatywne efekty z sojuszników.", "mana_cost": 25, "power": 0, "level": 5, "type": "buff"} ],

"Krwiścier": [
    {"name": "Rozbłysk Furii", "description": "Podwójne obrażenia przez jedną turę.", "mana_cost": 20, "power": 40, "level": 2, "type": "active"},
    {"name": "Krzyk Wojenny", "description": "Zwiększa siłę ataku sojuszników o 15%.", "mana_cost": 10, "power": 0, "level": 1, "type": "buff"},
    {"name": "Cios Rozpłatania", "description": "Przebija pancerz wroga.", "mana_cost": 18, "power": 50, "level": 3, "type": "active"},
    {"name": "Pancerz Gniewu", "description": "Zwiększa pancerz o 20% przez 2 tury.", "mana_cost": 14, "power": 0, "level": 2, "type": "buff"},
    {"name": "Uderzenie Krwi", "description": "Zadaje obrażenia i leczy za połowę.", "mana_cost": 20, "power": 30, "level": 4, "type": "active"},
    {"name": "Wola Przodków", "description": "Przywraca 25% many.", "mana_cost": 0, "power": 0, "level": 5, "type": "buff"}
],

"Wiedźcior": [
    {"name": "Szept Wilków", "description": "Zwiększa szansę uniku o 20%.", "mana_cost": 8, "power": 0, "level": 2, "type": "buff"},
    {"name": "Zmysły Bestii", "description": "Kontruje pierwszy cios.", "mana_cost": 12, "power": 15, "level": 3, "type": "active"},
    {"name": "Znak Igni", "description": "Miot ognia zadający obrażenia wszystkim wrogom.", "mana_cost": 18, "power": 30, "level": 4, "type": "active"},
    {"name": "Refleks Mutanta", "description": "Więcej ataków w tej rundzie.", "mana_cost": 10, "power": 0, "level": 3, "type": "buff"},
    {"name": "Znak Yrden", "description": "Spowalnia wroga.", "mana_cost": 15, "power": 10, "level": 4, "type": "active"},
    {"name": "Oczyszczenie", "description": "Usuwa wszystkie negatywne efekty.", "mana_cost": 20, "power": 0, "level": 5, "type": "buff"}
],

"Mrokorzyt": [
    {"name": "Zew Umarłych", "description": "Przyzywa martwego do ataku.", "mana_cost": 18, "power": 35, "level": 3, "type": "active"},
    {"name": "Kościane Więzy", "description": "Unieruchamia przeciwnika.", "mana_cost": 16, "power": 0, "level": 2, "type": "buff"},
    {"name": "Blask Krypt", "description": "Zadaje obrażenia obszarowe od cienia.", "mana_cost": 20, "power": 40, "level": 4, "type": "active"},
    {"name": "Wieczne Lamenty", "description": "Zwiększa moc zaklęć o 25% przez 2 tury.", "mana_cost": 15, "power": 0, "level": 3, "type": "buff"},
    {"name": "Nekrosfera", "description": "Obszar klątw.", "mana_cost": 25, "power": 35, "level": 5, "type": "active"},
    {"name": "Szept Grobu", "description": "Zmniejsza obrażenia otrzymywane o 15%.", "mana_cost": 10, "power": 0, "level": 2, "type": "buff"}
],

"Stryłecznik": [
    {"name": "Strzała Mgły", "description": "Strzała zwiększająca szansę trafienia krytycznego.", "mana_cost": 10, "power": 20, "level": 1, "type": "active"},
    {"name": "Ukrycie w Cieniu", "description": "Unik przez 1 rundę.", "mana_cost": 8, "power": 0, "level": 2, "type": "buff"},
    {"name": "Cios z Zaskoczenia", "description": "Podwójne obrażenia, jeśli wróg nie atakował.", "mana_cost": 15, "power": 35, "level": 3, "type": "active"},
    {"name": "Zatruta Strzała", "description": "Zadaje obrażenia przez 3 tury.", "mana_cost": 12, "power": 10, "level": 3, "type": "active"},
    {"name": "Skrytobójstwo", "description": "Natychmiastowa eliminacja słabego wroga.", "mana_cost": 20, "power": 50, "level": 5, "type": "active"},
    {"name": "Mistyfikacja", "description": "Zamienia miejscami z klonem.", "mana_cost": 18, "power": 0, "level": 4, "type": "buff"}
],

"Zielarzec": [
    {"name": "Napój Kruka", "description": "Leczy 25% HP.", "mana_cost": 10, "power": -25, "level": 1, "type": "buff"},
    {"name": "Korzenna Osłona", "description": "Zwiększa odporność na trucizny.", "mana_cost": 8, "power": 0, "level": 2, "type": "buff"},
    {"name": "Wywar Wilczura", "description": "Zadaje obrażenia bestiom.", "mana_cost": 14, "power": 30, "level": 3, "type": "active"},
    {"name": "Zgnilizna", "description": "Wrogowie otrzymują obrażenia co turę.", "mana_cost": 16, "power": 25, "level": 4, "type": "active"},
    {"name": "Eliksir Spokoju", "description": "Zmniejsza agresję wroga.", "mana_cost": 12, "power": 0, "level": 2, "type": "buff"},
    {"name": "Wyciszenie", "description": "Uniemożliwia rzucanie czarów.", "mana_cost": 15, "power": 0, "level": 3, "type": "active"}
],

"Snemistrz": [
    {"name": "Mgła Sennych Cieni", "description": "Wróg nie trafia przez 1 turę.", "mana_cost": 15, "power": 0, "level": 2, "type": "buff"},
    {"name": "Szepczące Przestrzenie", "description": "Przyspieszenie regeneracji many.", "mana_cost": 12, "power": 0, "level": 2, "type": "buff"},
    {"name": "Sen Wiecznego Kamienia", "description": "Uśpia przeciwnika.", "mana_cost": 18, "power": 0, "level": 3, "type": "active"},
    {"name": "Spaczenie Pamięci", "description": "Wrogi gracz zapomina czar.", "mana_cost": 25, "power": 0, "level": 5, "type": "active"},
    {"name": "Objawienie", "description": "Odsłania ukrytych przeciwników.", "mana_cost": 10, "power": 0, "level": 2, "type": "buff"},
    {"name": "Sny Cierpienia", "description": "Zadaje obrażenia psychiczne.", "mana_cost": 20, "power": 35, "level": 4, "type": "active"}
]

}

