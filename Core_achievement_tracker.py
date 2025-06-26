from achievement_tracker import AchievementSystem, AchievementTracker

achievement_system = AchievementSystem()
player_tracker = AchievementTracker(player_id="user123")

# Gdy gracz wykona coś istotnego:
if not player_tracker.has_achievement(1):
    player_tracker.unlock(1)
    print("Zdobyto osiągnięcie: Pierwsza Krew!")
    player_tracker.save("save/user123_achievements.json")
