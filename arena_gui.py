# arena_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from arena import ArenaBattle, ARENA_TYPES
from player import current_player

class ArenaGUI:
    def __init__(self, root, player):
        self.root = root
        self.player = player
        self.root.title("Arena Walki – Firos")
        self.root.geometry("680x500")
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self.root, text="🛡️ Arena Walki – Firos: Magic & Magic", font=("Garamond", 18, "bold"))
        title.pack(pady=10)

        self.type_label = ttk.Label(self.root, text="Wybierz typ Areny:")
        self.type_label.pack()

        self.arena_type_var = tk.StringVar()
        self.arena_dropdown = ttk.Combobox(self.root, textvariable=self.arena_type_var, values=ARENA_TYPES, state="readonly", width=30)
        self.arena_dropdown.current(0)
        self.arena_dropdown.pack(pady=5)

        self.start_button = ttk.Button(self.root, text="Rozpocznij Pojedynek", command=self.start_battle)
        self.start_button.pack(pady=10)

        self.output_text = tk.Text(self.root, height=20, width=80, bg="#191919", fg="#EEE", font=("Courier", 10))
        self.output_text.pack(pady=10)

    def start_battle(self):
        arena_type = self.arena_type_var.get()
        self.output_text.delete("1.0", tk.END)

        self.output_text.insert(tk.END, f"🔷 Rozpoczynasz walkę na Arenie: {arena_type}\n")
        battle = ArenaBattle(self.player, arena_type=arena_type, is_ranked=True)
        result = battle.start_battle()

        for line in result:
            self.output_text.insert(tk.END, line + "\n")
        self.output_text.insert(tk.END, "\n🎖️ Walka zakończona. Gratulacje!\n")

def launch_arena_gui(player=None):
    if player is None:
        player = current_player  # domyślnie globalny gracz
    root = tk.Tk()
    app = ArenaGUI(root, player)
    root.mainloop()

# Testowe uruchomienie GUI (można zakomentować w grze)
# if __name__ == "__main__":
#     from player import current_player
#     launch_arena_gui(current_player)
