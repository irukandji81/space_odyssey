from assets.characters import create_character
from assets.locations import starting_location
from utils.save_load import save_game, load_game

def main():
    print("Welcome to Space Odyssey!")
    print("1. Start a New Game")
    print("2. Load a Saved Game")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        player = create_character()
        starting_location(player)
    elif choice == "2":
        player = load_game()
        if player:
            starting_location(player)
        else:
            print("No saved game found. Starting a new game...")
            player = create_character()
            starting_location(player)
    else:
        print("Invalid choice. Exiting...")
    
    save_game(player)

if __name__ == "__main__":
    main()
