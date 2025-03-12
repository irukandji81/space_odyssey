def create_character():
    print("Creating your character...")
    name = input("Enter your character's name: ")
    print("Choose your profession:")
    print("1. Engineer")
    print("2. Pilot")
    print("3. Scientist")
    profession_choice = input("Enter your choice: ")
    
    professions = {
        "1": {"profession": "Engineer", "health": 120, "skills": ["Repair"]},
        "2": {"profession": "Pilot", "health": 100, "skills": ["Evasion"]},
        "3": {"profession": "Scientist", "health": 90, "skills": ["Analysis"]}
    }
    
    player = {
        "name": name,
        **professions.get(profession_choice, {"profession": "Unknown", "health": 100, "skills": []}),
        "inventory": []
    }
    print(f"Welcome, {name} the {player['profession']}! Your journey begins...")
    return player

def combat(player, enemy):
    print(f"\nA wild {enemy['name']} appears!")
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"Your health: {player['health']}, {enemy['name']} health: {enemy['health']}")
        print("1. Attack")
        print("2. Run")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"You attack the {enemy['name']}!")
            enemy["health"] -= 20
            print(f"The {enemy['name']} attacks you!")
            player["health"] -= enemy["damage"]
        elif choice == "2":
            print("You escape safely!")
            return
        else:
            print("Invalid choice.")
    
    if player["health"] <= 0:
        print("You have been defeated. Game over.")
    elif enemy["health"] <= 0:
        print(f"You defeated the {enemy['name']}!")
