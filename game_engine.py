class GameEngine:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            print("Gra działa... Wybierz opcję z menu.")
            command = input("> ").strip().lower()

            if command == "exit":
                print("Zamykanie gry...")
                self.running = False
            else:
                print(f"Nieznane polecenie: {command}")
