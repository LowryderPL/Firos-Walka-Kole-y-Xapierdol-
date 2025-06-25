guilds.py – System Gildii (FIROS: Magic & Magic)

Autor: System FIROS

Status: Szkielet – do uzupełnienia i rozszerzenia

import uuid import datetime

class Guild: def init(self, name, leader_id): self.id = str(uuid.uuid4()) self.name = name self.leader_id = leader_id self.members = {leader_id: "Leader"} self.gold = 0 self.points = 0 self.guild_level = 1 self.guild_bank = {} self.quests_completed = [] self.bosses_defeated = [] self.upgrades = [] self.logs = []

def add_member(self, user_id, role="Member"):
    if user_id not in self.members:
        self.members[user_id] = role
        self.logs.append(f"[{datetime.datetime.now()}] {user_id} joined guild.")

def remove_member(self, user_id):
    if user_id in self.members:
        del self.members[user_id]
        self.logs.append(f"[{datetime.datetime.now()}] {user_id} removed from guild.")

def donate_gold(self, user_id, amount):
    self.gold += amount
    self.logs.append(f"[{datetime.datetime.now()}] {user_id} donated {amount} gold.")

def upgrade_guild(self, upgrade_name, cost):
    if self.gold >= cost:
        self.gold -= cost
        self.upgrades.append(upgrade_name)
        self.guild_level += 1
        self.logs.append(f"[{datetime.datetime.now()}] Guild upgraded with {upgrade_name}.")

def complete_quest(self, quest_id):
    self.quests_completed.append(quest_id)
    self.points += 10
    self.logs.append(f"[{datetime.datetime.now()}] Guild completed quest {quest_id}.")

def defeat_boss(self, boss_name):
    self.bosses_defeated.append(boss_name)
    self.points += 50
    self.logs.append(f"[{datetime.datetime.now()}] Boss {boss_name} defeated.")

def status(self):
    return {
        "name": self.name,
        "leader": self.leader_id,
        "level": self.guild_level,
        "members": len(self.members),
        "gold": self.gold,
        "points": self.points,
        "upgrades": self.upgrades,
    }

GuildsManager – zarządzanie wszystkimi gildiami

class GuildsManager: def init(self): self.guilds = {}

def create_guild(self, name, leader_id):
    guild = Guild(name, leader_id)
    self.guilds[guild.id] = guild
    return guild.id

def get_guild(self, guild_id):
    return self.guilds.get(guild_id)

def list_guilds(self):
    return [{"id": gid, **g.status()} for gid, g in self.guilds.items()]

def donate_to_guild(self, guild_id, user_id, amount):
    guild = self.get_guild(guild_id)
    if guild:
        guild.donate_gold(user_id, amount)

def upgrade_guild(self, guild_id, upgrade_name, cost):
    guild = self.get_guild(guild_id)
    if guild:
        guild.upgrade_guild(upgrade_name, cost)

def run_guild_boss_battle(self, guild_id, boss_name):
    guild = self.get_guild(guild_id)
    if guild:
        guild.defeat_boss(boss_name)

