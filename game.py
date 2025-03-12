from assets.characters import create_character
from assets.locations import (
    cryo_chamber, engineering_room, med_bay, cargo_hold,
    bridge, observation_deck, quarters, reactor_core, armory,
    communications_room, storage_bay, escape_pods,
    maintenance_shafts, alien_containment_unit, cockpit
)
from utils.save_load import save_game, load_game
from utils.helpers import reactor_core_puzzle, alien_signal_puzzle
from utils.menu import main_action_menu, check_inventory

def room_selector(player):
    print("\nYou are currently in the spaceship. Choose your next destination:")
    rooms = [
        "Cockpit", "Engineering Room", "Med Bay", "Cryo Chamber",
        "Cargo Hold", "Bridge", "Observation Deck", "Quarters",
        "Reactor Core", "Armory", "Communications Room", "Storage Bay",
        "Escape Pods", "Maintenance Shafts", "Alien Containment Unit"
    ]
    for index, room in enumerate(rooms, start=1):
        print(f"{index}. {room}")
    
    choice = input("Enter the number of the room you want to visit: ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(rooms):
            return rooms[choice_index].replace(" ", "_").lower()
        else:
            print("Invalid choice. Try again.")
            return room_selector(player)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return room_selector(player)

def main_game_loop(player):
    current_room = "cockpit"  # Start in the cockpit
    
    while True:
        if current_room == "cockpit":
            next_room = cockpit(player)
        elif current_room == "engineering_room":
            next_room = engineering_room(player)
        elif current_room == "med_bay":
            next_room = med_bay(player)
        elif current_room == "cryo_chamber":
            next_room = cryo_chamber(player)
        elif current_room == "cargo_hold":
            next_room = cargo_hold(player)
        elif current_room == "bridge":
            next_room = bridge(player)
        elif current_room == "observation_deck":
            next_room = observation_deck(player)
        elif current_room == "quarters":
            next_room = quarters(player)
        elif current_room == "reactor_core":
            next_room = reactor_core(player)
        elif current_room == "armory":
            next_room = armory(player)
        elif current_room == "communications_room":
            next_room = communications_room(player)
        elif current_room == "storage_bay":
            next_room = storage_bay(player)
        elif current_room == "escape_pods":
            next_room = escape_pods(player)
        elif current_room == "maintenance_shafts":
            next_room = maintenance_shafts(player)
        elif current_room == "alien_containment_unit":
            next_room = alien_containment_unit(player)
        elif current_room == "room_selector":
            current_room = room_selector(player)  # Show move menu
            continue
        else:
            print("Room functionality not implemented yet.")
            break

        if next_room == "room_selector":
            current_room = room_selector(player)
        else:
            current_room = next_room

def main():
    print("Welcome to Space Odyssey!")
    print("1. Start a New Game")
    print("2. Load a Saved Game")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        player = create_character()
        main_game_loop(player)
    elif choice == "2":
        player = load_game()
        if player:
            main_game_loop(player)
        else:
            print("No saved game found. Starting a new game...")
            player = create_character()
            main_game_loop(player)
    else:
        print("Invalid choice. Exiting...")
    
    print("Thanks for playing Space Odyssey!")
    save_game(player)

if __name__ == "__main__":
    main()
