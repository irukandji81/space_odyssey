import json

def save_game(player):
    with open("data/save_data.json", "w") as file:
        json.dump(player, file)
    print("Game saved successfully!")

def load_game():
    try:
        with open("data/save_data.json", "r") as file:
            player = json.load(file)
        print("Game loaded successfully!")
        return player
    except FileNotFoundError:
        print("No saved game data found.")
        return None
