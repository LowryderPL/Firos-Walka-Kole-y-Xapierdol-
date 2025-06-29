from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

### === CRAFTING ENDPOINT === ###
@app.route("/api/crafting", methods=["GET"])
def get_recipes():
    conn = sqlite3.connect("firos_inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, ingredients, effect FROM crafting_recipes")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {
            "id": row[0],
            "name": row[1],
            "ingredients": row[2].split(','),
            "effect": row[3]
        } for row in rows
    ])

### === INVENTORY ENDPOINT === ###
@app.route("/api/inventory", methods=["GET"])
def get_inventory():
    conn = sqlite3.connect("firos_inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, rarity, power, defense, magic FROM inventory")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "rarity": row[3],
            "power": row[4],
            "defense": row[5],
            "magic": row[6]
        } for row in rows
    ])

### === QUESTY ENDPOINT === ###
@app.route("/api/quests", methods=["GET"])
def get_quests():
    conn = sqlite3.connect("firos_inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, reward FROM quests")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "reward": row[3]
        } for row in rows
    ])

if __name__ == "__main__":
    app.run(debug=True)
