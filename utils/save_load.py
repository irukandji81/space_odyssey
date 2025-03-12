import json

def save_game(player):
    with open("data/save_data.json", "w") as file:
        json.dump(player, file)
    print("Game saved successfully!")

def load_game():
    try:
        with open("data/save_data.json", "r") as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Empty save file.")
            player = json.loads(content)
        print("Game loaded successfully!")
        return player
    except FileNotFoundError:
        print("No saved game data found.")
        return None
    except (ValueError, json.JSONDecodeError):
        print("Save file is corrupted or empty. Starting a new game...")
        return None
