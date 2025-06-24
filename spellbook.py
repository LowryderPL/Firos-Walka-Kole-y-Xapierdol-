spellbook.py – Pełna baza czarów dla gry Firos: Magic & Magic

Struktura: każda klasa posiada 10 unikalnych czarów, rosnących poziomem, mocą i wymaganiami

spells_data = { "Mag Ognia": [ {"name": "Iskra Żarwena", "level": 1, "type": "ogień", "mana": 10, "power": 15, "description": "Wypuszcza iskrę ognia, która podpala cel."}, {"name": "Płomień Przodków", "level": 2, "type": "ogień", "mana": 12, "power": 18, "description": "Ognisty atak ze wspomnieniem pradawnych."}, {"name": "Krąg Słońca", "level": 3, "type": "ogień", "mana": 15, "power": 22, "description": "Tworzy krąg ognia wokół gracza."}, {"name": "Żar Wilczycy", "level": 4, "type": "ogień", "mana": 20, "power": 30, "description": "Zaklęcie ognia o wilczej zaciekłości."}, {"name": "Płomień Swarożyca", "level": 5, "type": "ogień", "mana": 25, "power": 35, "description": "Potężny ogień boga dawnych plemion."}, {"name": "Smoczy Ryk", "level": 6, "type": "ogień", "mana": 30, "power": 42, "description": "Zaklęcie przypominające ryk smoka."}, {"name": "Pochodnia Wieczności", "level": 7, "type": "ogień", "mana": 32, "power": 45, "description": "Wieczny płomień, który nie gaśnie."}, {"name": "Miedziana Gardziel", "level": 8, "type": "ogień", "mana": 35, "power": 50, "description": "Otwiera szczelinę piekielną."}, {"name": "Zew Płomiennego Tronu", "level": 9, "type": "ogień", "mana": 40, "power": 55, "description": "Przywołanie ognistego władcy."}, {"name": "Smok Wulkaniczny", "level": 10, "type": "ogień", "mana": 45, "power": 65, "description": "Najpotężniejsze zaklęcie ognia przywołujące bestię."} ],

"Mag Lodu": [
    {"name": "Szron Dziadosza", "level": 1, "type": "lód", "mana": 9, "power": 12, "description": "Zamraża wroga na chwilę."},
    {"name": "Zlodź Opuszcza", "level": 2, "type": "lód", "mana": 11, "power": 16, "description": "Lodowy pocisk trafia losowy cel."},
    {"name": "Mgła Welesowa", "level": 3, "type": "lód", "mana": 15, "power": 20, "description": "Mgła lodu otacza pole bitwy."},
    {"name": "Pazury Zimy", "level": 4, "type": "lód", "mana": 18, "power": 25, "description": "Zaklęcie lodowego szpona."},
    {"name": "Zimowy Krąg", "level": 5, "type": "lód", "mana": 22, "power": 30, "description": "Krąg lodu spowalniający wrogów."},
    {"name": "Sople Nawii", "level": 6, "type": "lód", "mana": 26, "power": 35, "description": "Przywołuje ostre sople lodu."},
    {"name": "Wiatr Buranowy", "level": 7, "type": "lód", "mana": 30, "power": 38, "description": "Potężny lodowy wiatr uderza przeciwników."},
    {"name": "Zamieć Przodków", "level": 8, "type": "lód", "mana": 33, "power": 41, "description": "Przywołuje duchy burz śnieżnych."},
    {"name": "Królestwo Mrozu", "level": 9, "type": "lód", "mana": 35, "power": 47, "description": "Całkowicie zamraża dużą część pola."},
    {"name": "Sędzia Lodowej Otchłani", "level": 10, "type": "lód", "mana": 40, "power": 55, "description": "Ostateczny wyrok mrozu."}
]
# Analogiczne wpisy dla klas: Nekromanta, Alchemik, Mutant, Wojownik, Łucznik, Wiedzący

}

def get_spells_for_class(class_name): return spells_data.get(class_name, [])

def get_spell_by_name(class_name, spell_name): spells = get_spells_for_class(class_name) return next((s for s in spells if s["name"] == spell_name), None)

def list_all_spells(): return [(cls, spell["name"]) for cls in spells_data for spell in spells_data[cls]]

