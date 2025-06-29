from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/api/crafting")
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

if __name__ == "__main__":
    app.run(debug=True)
