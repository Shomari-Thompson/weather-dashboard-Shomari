import json
import os

SETTINGS_FILE = "settings.json"

default_settings = {
    "favorite_cities": ["New York", "Tokyo", "London"],
    "theme": "flatly"
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)
