class Beast:
    def __init__(self, name, description, hp, attack):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack

    def show_info(self):
        print(f"\n👹 {self.name}")
        print(f"Opis: {self.description}")
        print(f"Punkty życia: {self.hp}")
        print(f"Atak: {self.attack}")


class Bestiary:
    def __init__(self):
        self.beasts = [
            Beast("Wilczy Cień", "Upiorny wilk grasujący w cieniu lasu. Uważaj na jego kły.", 20, 5),
            Beast("Wędrowny Ghul", "Były człowiek, teraz rozszarpujący nocą podróżników.", 25, 7),
            Beast("Słony Demon", "Demon z podziemi Thalinu, zieje toksyczną mgłą.", 30, 9),
            Beast("Ognisty Widmowąż", "
