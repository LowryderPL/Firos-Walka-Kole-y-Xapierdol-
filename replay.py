# replay.py — System powtórek FIROS

import json
import os
import datetime

class ReplayManager:
    def __init__(self, folder="replays"):
        self.folder = folder
        self.recording = []
        self.playback = []
        self.playing = False
        self.index = 0

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def record_action(self, action_data):
        if isinstance(action_data, dict):
            timestamp = datetime.datetime.now().isoformat()
            self.recording.append({"timestamp": timestamp, "action": action_data})

    def save(self, match_id=None):
        if not self.recording:
            return

        match_id = match_id or datetime.datetime.now().strftime("match_%Y%m%d_%H%M%S")
        filepath = os.path.join(self.folder, f"{match_id}.replay.json")

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.recording, f, indent=4)

        self.recording = []  # Clear after saving

    def load(self, filename):
        filepath = os.path.join(self.folder, filename)
        if not os.path.exists(filepath):
            print(f"[Replay] Nie znaleziono pliku: {filename}")
            return

        with open(filepath, "r", encoding="utf-8") as f:
            self.playback = json.load(f)

        self.playing = True
        self.index = 0
        print(f"[Replay] Załadowano powtórkę: {filename}")

    def update(self, display_callback):
        if not self.playing or self.index >= len(self.playback):
            return

        action = self.playback[self.index]["action"]
        display_callback(action)
        self.index += 1

        if self.index >= len(self.playback):
            self.playing = False
            print("[Replay] Powtórka zakończona")

    def list_replays(self):
        return [f for f in os.listdir(self.folder) if f.endswith(".replay.json")]

    def is_playing(self):
        return self.playing
