from inventory import inventory

class GameEngine:
    def __init__(self):
        self.action_points = 5

    def run(self):
        print("\n=== ROZPOCZYNAMY GRĘ ===")
        print(f"Masz {self.action_points} punktów akcji.\n")

        while self.action_points > 0:
            print("1. Wyrusz na misję")
            print("2. Odpocznij")
            print("3. Zakończ turę")

            choice = input("Wybierz akcję (1-3): ").strip()

            if choice == "1":
                self.start_mission()
            elif choice == "2":
                self.rest()
            elif choice == "3":
                print("Zakończyłeś turę.")
                break
            else:
                print("Nieprawidłowy wybór.\n")

        if self.action_points <= 0:
            print("Skończyły Ci się punkty akcji. Musisz odpocząć.")

    def start_mission(self):
        print("\n> Rozpocząłeś misję: Cień Nad Wioską")
        print("Napotykasz dzikiego potwora – Wilczy Cień!")
        print("🔥 Walka!")

        wynik = input("Czy chcesz zaatakować? (t/n): ").strip().lower()
        if wynik == "t":
            print("Udało Ci się pokonać potwora! Zdobywasz nagrody.")
            self.action_points -= 2
        else:
            print("Uciekasz z pola walki...")
            self.action_points -= 1

    def rest(self):
        print("Odpoczywasz przy ognisku...")
        self.action_points += 2
        print(f"Odzyskano 2 punkty. Obecnie masz: {self.action_points}")
