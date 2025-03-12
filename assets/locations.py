def starting_location(player):
    print("\nYou wake up in the cockpit of an abandoned spaceship.")
    print("1. Inspect the control panel.")
    print("2. Search for supplies.")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("You find a strange device emitting a soft blue glow...")
        player["inventory"].append("Mysterious Device")
    elif choice == "2":
        print("You find some rations and a medkit.")
        player["inventory"].extend(["Rations", "Medkit"])
    else:
        print("You hesitate... time passes.")

    print(f"Current Inventory: {player['inventory']}")
