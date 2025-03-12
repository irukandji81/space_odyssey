def create_character():
    print("Creating your character...")
    name = input("Enter your character's name: ")
    player = {
        "name": name,
        "health": 100,
        "inventory": []
    }
    print(f"Welcome, {name}! Your journey begins...")
    return player
