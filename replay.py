# core/replay.py

import time

class ReplayManager:
    def __init__(self):
        self.moves = []
        self.replaying = False
        self.index = 0

    def record_move(self, move_data):
        """Zapisuje ruch w formie słownika."""
        self.moves.append(move_data)

    def start(self, board):
        """Rozpoczyna odtwarzanie zresetowanego stanu planszy."""
        if not self.moves:
            print("Brak ruchów do odtworzenia.")
            return
        self.replaying = True
        self.index = 0
        board.reset_board()

    def update(self, screen=None):
        """Odtwarza ruchy krok po kroku."""
        if self.replaying and self.index < len(self.moves):
            move = self.moves[self.index]
            self._apply_move(move)
            self.index += 1
            time.sleep(0.5)  # tempo odtwarzania
        elif self.index >= len(self.moves):
            self.replaying = False

    def _apply_move(self, move):
        # Przykład struktury ruchu: {"from": (x1, y1), "to": (x2, y2),
