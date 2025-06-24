# spellbook.py — Pełna baza zaklęć dla klas w Firos: Magic & Magic

# Struktura: każda klasa posiada 10 unikalnych czarów, rosnących poziomem, mocą i wymaganiami

spells_data = {
    "Mag Ognia": [
        {"name": "Iskra Żarwena", "level": 1, "type": "ogień", "mana": 10, "power": 15, "description": "Wypuszcza iskrę ognia, która podpala przeciwnika"},
        {"name": "Płomień Przodków", "level": 2, "type": "ogień", "mana": 12, "power": 18, "description": "Ognisty atak duchów przodków"},
        {"name": "Krąg Słońca", "level": 3, "type": "ogień", "mana": 15, "power": 22, "description": "Tworzy krąg ognia wokół postaci"},
        {"name": "Żar Wilczycy", "level": 4, "type": "ogień", "mana": 18, "power": 27, "description": "Zaklęcie ognistej wilczycy"},
        {"name": "Płomień Svaroga", "level": 5, "type": "ogień", "mana": 20, "power": 33, "description": "Ogień boga Svaroga uderza we wrogów"},
        {"name": "Smoczy Pomruk", "level": 6, "type": "ogień", "mana": 23, "power": 37, "description": "Przywołuje smoczy oddech"},
        {"name": "Miecz Płomienia", "level": 7, "type": "ogień", "mana": 26, "power": 41, "description": "Zaklęcie tworzy płonący miecz"},
        {"name": "Infernalna Gardziel", "level": 8, "type": "ogień", "mana": 30, "power": 48, "description": "Otwiera szczelinę piekielną"},
        {"name": "Zew Płomiennego Tronu", "level": 9, "type": "ogień", "mana": 35, "power": 54, "description": "Wzywa ognistego króla"},
        {"name": "Płomień Końca Dni", "level": 10, "type": "ogień", "mana": 40, "power": 60, "description": "Ostateczne zaklęcie ognia"}
    ],
    "Mag Lodu": [
        {"name": "Szron Dziadosza", "level": 1, "type": "lód", "mana": 9, "power": 12, "description": "Zamraża wroga na chwilę"},
        {"name": "Zlodź Opuszcza", "level": 2, "type": "lód", "mana": 11, "power": 16, "description": "Lodowy pocisk trafia losowo"},
        {"name": "Mgła Welesowa", "level": 3, "type": "lód", "mana": 14, "power": 20, "description": "Otacza pole bitwy mgłą"},
        {"name": "Pazury Zimy", "level": 4, "type": "lód", "mana": 18, "power": 25, "description": "Szarpie przeciwników lodem"},
        {"name": "Zimowy Krąg", "level": 5, "type": "lód", "mana": 21, "power": 30, "description": "Tworzy barierę lodową"},
        {"name": "Sople Nawii", "level": 6, "type": "lód", "mana": 25, "power": 34, "description": "Przywołuje sople z zaświatów"},
        {"name": "Wiatr Buranowy", "level": 7, "type": "lód", "mana": 26, "power": 36, "description": "Uderza wrogów burzą śnieżną"},
        {"name": "Zamieć Przodków", "level": 8, "type": "lód", "mana": 30, "power": 41, "description": "Przywołuje duchy burz śnieżnych"},
        {"name": "Królestwo Mrozu", "level": 9, "type": "lód", "mana": 35, "power": 47, "description": "Zamraża całą mapę wokół"},
        {"name": "Sędzia Lodowej Otchłani", "level": 10, "type": "lód", "mana": 40, "power": 55, "description": "Wyrok śmierci z lodu"}
    ]
}

# Można dynamicznie rozwijać zaklęcia w grze na podstawie tej bazy i przypisać je do klas.
