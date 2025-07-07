import json
import os

DB_PATH = "users.json"

def load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def get_user(discord_id):
    users = load_db()
    return next((u for u in users if u["discord_id"] == discord_id), None)

def get_all_users():
    return load_db()

def add_user(discord_id, notify_mode):
    users = load_db()
    user = get_user(discord_id)
    if user:
        user["notify"] = notify_mode
    else:
        users.append({"discord_id": discord_id, "notify": notify_mode, "puuid": "dummy-puuid"})
    save_db(users)