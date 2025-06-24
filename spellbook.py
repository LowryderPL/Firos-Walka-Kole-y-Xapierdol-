spellbook.py — Pełna baza zaklęć dla klas w Firos: Magic & Magic

Struktura: każda klasa posiada 10 unikalnych czarów, rosnących poziomem, mocą i wymaganiami

spells_data = { "Mag Ognia": [ {"name": "Iskra Żarwena", "level": 1, "type": "ogień", "mana": 10, "power": 15, "description": "Wypuszcza iskrę ognia, która podpala przeciwnika."}, {"name": "Płomień Przodków", "level": 2, "type": "ogień", "mana": 12, "power": 18, "description": "Płomień odziedziczony po przodkach uderza z nieba."}, {"name": "Krąg Słońca", "level": 3, "type": "ogień", "mana": 15, "power": 22, "description": "Tworzy krąg ognia wokół wroga."}, {"name": "Żar Wilczycy", "level": 4, "type": "ogień", "mana": 18, "power": 28, "description": "Zaklęcie ognistej wilczycy — podwójne obrażenia."}, {"name": "Płomień Swarożyca", "level": 5, "type": "ogień", "mana": 20, "power": 35, "description": "Święty ogień boga Swarożyca uderza przeciwników."}, {"name": "Smoczy Pomruk", "level": 6, "type": "ogień", "mana": 24, "power": 42, "description": "Przywołuje smoczy oddech ognia."}, {"name": "Miedziana Gardziel", "level": 7, "type": "ogień", "mana": 27, "power": 48, "description": "Otwiera szczelinę piekielnego płomienia."}, {"name": "Żar Cienia", "level": 8, "type": "ogień", "mana": 30, "power": 53, "description": "Zaklęcie ognia ukrytego w cieniach."}, {"name": "Słup Spalenia", "level": 9, "type": "ogień", "mana": 36, "power": 58, "description": "Kolumna ognia przebija niebo i ziemię."}, {"name": "Zew Płomiennego Tronu", "level": 10, "type": "ogień", "mana": 42, "power": 60, "description": "Ostateczne zaklęcie ognistego władcy."} ],

"Mag Lodu": [
    {"name": "Szron Dziadosza", "level": 1, "type": "lód", "mana": 9, "power": 12, "description": "Zamarza wroga na chwilę, spowalniając go."},
    {"name": "Zlodź Opuszcza", "level": 2, "type": "lód", "mana": 11, "power": 16, "description": "Lodowy pocisk trafia losowego przeciwnika."},
    {"name": "Mgła Welesowa", "level": 3, "type": "lód", "mana": 13, "power": 20, "description": "Mgła lodu otacza pole bitwy, zmniejszając widoczność."},
    {"name": "Pazury Zimy", "level": 4, "type": "lód", "mana": 15, "power": 23, "description": "Zaklęcie lodowego szpona szarpie przeciwnika."},
    {"name": "Zimowy Krąg", "level": 5, "type": "lód", "mana": 18, "power": 27, "description": "Tworzy pole lodu spowalniające wrogów."},
    {"name": "Sople Nawii", "level": 6, "type": "lód", "mana": 21, "power": 31, "description": "Przywołuje ostre sople lodu z zaświatów."},
    {"name": "Wiatr Buranowy", "level": 7, "type": "lód", "mana": 26, "power": 36, "description": "Potężny lodowy wiatr uderza wrogów."},
    {"name": "Zamieć Przodków", "level": 8, "type": "lód", "mana": 30, "power": 41, "description": "Przywołuje duchy burz śnieżnych z przeszłości."},
    {"name": "Królestwo Mrozu", "level": 9, "type": "lód", "mana": 35, "power": 47, "description": "Całkowicie zamraża dużą część mapy."},
    {"name": "Sędzia Lodowej Otchłani", "level": 10, "type": "lód", "mana": 40, "power": 55, "description": "Ostateczny wyrok mrozu na wroga."}
]

# Dodaj tutaj pozostałe klasy: Nekromanta, Alchemik, Mutant, Wojownik, Łucznik, Wiedzący
# Każda z nich powinna mieć strukturę analogiczną z listą 10 zaklęć

}

Można dynamicznie rozwinąć zaklęcia w grze na podstawie tej bazy i przypisać je do klas.

