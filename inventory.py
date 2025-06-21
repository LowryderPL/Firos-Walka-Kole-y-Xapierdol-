class Inventory:
    def __init__(self):
        self.items = ["Miecz żelazny", "Zbroja skórzana", "Mikstura leczenia"]

    def show(self):
        print("\n=== TWÓJ EKWIPUNEK ===")
        if not self.items:
            print("Pusto jak w sakwie wieśniaka.")
        else:
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item}")

    def add_item(self, item):
        self.items.append(item)
        print(f"Zyskano przedmiot: {item}")

    def remove_item(self, index):
        try:
            removed = self.items.pop(index - 1)
            print(f"Usunięto przedmiot: {removed}")
        except IndexError:
            print("Nieprawidłowy numer przedmiotu.")


# globalna instancja do użycia w grze
inventory = Inventory()


def show_inventory():
    inventory.show()
