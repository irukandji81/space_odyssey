def check_inventory(player):
    print("\nYour current inventory:")
    if player["inventory"]:
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

def main_action_menu(player):
    print("\nWhat would you like to do next?")
    print("1. Continue in the current room.")
    print("2. Check inventory.")
    print("3. Move to another room.")
    choice = input("Enter your choice: ")

    if choice == "1":
        return "stay"  # Stay in the current room
    elif choice == "2":
        check_inventory(player)
        return "action_menu"  # Return to the action menu
    elif choice == "3":
        return "move"  # Trigger the move menu
    else:
        print("Invalid choice.")
        return "action_menu"
