# core/save_load.py — system zapisu i wczytywania stanu gry (Szachy FIROS)

import json
import os

class SaveSystem:
    SAVE_PATH = "saves"

    def __init__(self):
        if not os.path.exists(self.SAVE_PATH):
            os.makedirs(self.SAVE_PATH)

    def save(self, board, filename="autosave.json"):
        data = {
            "turn": board.current_turn,
            "pieces": [
                {
                    "type": piece.type,
                    "team": piece.team,
                    "position": piece.position,
                    "status": piece.status
                } for piece in board.pieces
            ]
        }
        with open(os.path.join(self.SAVE_PATH, filename), "w") as f:
            json.dump(data, f, indent=4)

    def load(self, board, filename="autosave.json"):
        path = os.path.join(self.SAVE_PATH, filename)
        if not os.path.exists(path):
            print("Brak zapisu.")
            return
        with open(path, "r") as f:
            data = json.load(f)
            board.current_turn = data["turn"]
            board.pieces.clear()
            for p in data["pieces"]:
                board.add_piece(
                    piece_type=p["type"],
                    team=p["team"],
                    position=p["position"],
                    status=p.get("status", None)
                )
