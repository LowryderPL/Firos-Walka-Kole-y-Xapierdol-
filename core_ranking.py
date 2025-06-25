# core/ranking.py

class PlayerRanking:
    def __init__(self):
        self.rankings = {}

    def register_player(self, player_id, player_name):
        if player_id not in self.rankings:
            self.rankings[player_id] = {
                "name": player_name,
                "points": 1000,
                "wins": 0,
                "losses": 0,
                "matches": 0,
            }

    def record_match(self, winner_id, loser_id):
        if winner_id not in self.rankings or loser_id not in self.rankings:
            return

        self.rankings[winner_id]["points"] += 25
        self.rankings[winner_id]["wins"] += 1
        self.rankings[winner_id]["matches"] += 1

        self.rankings[loser_id]["points"] = max(0, self.rankings[loser_id]["points"] - 15)
        self.rankings[loser_id]["losses"] += 1
        self.rankings[loser_id]["matches"] += 1

    def get_top_players(self, limit=10):
        return sorted(
            self.rankings.items(),
            key=lambda item: item[1]["points"],
            reverse=True
        )[:limit]

    def get_player_stats(self, player_id):
        return self.rankings.get(player_id, None)

    def reset_rankings(self):
        for player in self.rankings.values():
            player["points"] = 1000
            player["wins"] = 0
            player["losses"] = 0
            player["matches"] = 0
