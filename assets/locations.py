from utils.menu import main_action_menu, check_inventory

def cockpit(player):
    while True:
        print("\nYou are in the Cockpit. The central console lights blink softly.")
        print("1. Inspect the control panel.")
        print("2. Search under the seats.")
        action = input("Enter your choice: ")

        if action == "1":
            print("The control panel is missing a critical navigational component. You need to find it elsewhere.")
        elif action == "2":
            print("You find a torn piece of a star map. This might come in handy later!")
            player["inventory"].append("Star Map Fragment")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"  # Player chooses to move
        elif next_step == "action_menu":
            continue  # Loop back to the action menu
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def engineering_room(player):
    while True:
        print("\nThe Engineering Room is filled with tangled wires and sparking consoles.")
        print("1. Inspect the engine.")
        print("2. Search for tools.")
        action = input("Enter your choice: ")

        if action == "1":
            if "Repair Kit" in player["inventory"]:
                print("You already have the Repair Kit! You can now repair the engine.")
            else:
                print("The engine is damaged and needs a Repair Kit to function. Keep looking for one!")
        elif action == "2":
            if "Repair Kit" not in player["inventory"]:
                print("You find a Repair Kit under a pile of debris.")
                player["inventory"].append("Repair Kit")
            else:
                print("You’ve already collected the Repair Kit.")
        else:
            print("Invalid choice.")
            continue

        # Handle the player's next action
        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room.")


def med_bay(player):
    while True:
        print("\nYou enter the Med Bay. The faint smell of antiseptic lingers in the air.")
        print("1. Search the cabinets.")
        print("2. Inspect the surgical table.")
        action = input("Enter your choice: ")

        if action == "1":
            print("The cabinets are locked. You need a passcode to open them.")
        elif action == "2":
            print("You find a medkit on the surgical table and add it to your inventory.")
            player["inventory"].append("Medkit")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def cryo_chamber(player):
    while True:
        print("\nThe Cryo Chamber houses rows of frozen crew members. The pods are malfunctioning, and frost clings to every surface.")
        print("1. Inspect the cryopods.")
        print("2. Access the control panel.")
        action = input("Enter your choice: ")

        if action == "1":
            print("The cryopods are frosted over. You need to stabilize the temperature.")
        elif action == "2":
            print("The control panel warns of critical failures. Solve the puzzle to stabilize the system.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def cargo_hold(player):
    while True:
        print("\nThe Cargo Hold is vast, with crates stacked haphazardly and strange noises echoing in the distance.")
        print("1. Open a crate.")
        print("2. Investigate the noise.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You find spare parts and add them to your inventory.")
            player["inventory"].append("Spare Parts")
        elif action == "2":
            print("You encounter a strange, scuttling creature. It hisses and runs away.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def bridge(player):
    while True:
        print("\nYou step onto the Bridge, where holographic displays flicker and static fills the speakers.")
        print("1. Inspect the captain's logs.")
        print("2. Attempt to access the navigation system.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You discover a log detailing the ship's last known coordinates. This could be useful.")
            player["inventory"].append("Captain's Log")
        elif action == "2":
            print("The navigation system is offline. You need the 'Star Map Fragment' to restore it.")
            if "Star Map Fragment" in player["inventory"]:
                print("You use the Star Map Fragment and successfully restore the navigation system!")
            else:
                print("You don't have the required item.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def observation_deck(player):
    while True:
        print("\nThe Observation Deck offers a breathtaking view of the galaxy.")
        print("1. Search for clues.")
        print("2. Use the telescope.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You find an encrypted note tucked behind a panel.")
            player["inventory"].append("Encrypted Note")
        elif action == "2":
            print("Using the telescope, you spot a distant planet that seems oddly familiar.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def quarters(player):
    while True:
        print("\nThe crew's Quarters are eerily empty, with overturned furniture and scattered belongings.")
        print("1. Search the lockers.")
        print("2. Examine the photographs on the wall.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You find a mysterious key inside one of the lockers.")
            player["inventory"].append("Mysterious Key")
        elif action == "2":
            print("The photographs reveal happier times, but one crew member's face is scratched out.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def reactor_core(player):
    while True:
        print("\nThe Reactor Core hums faintly, barely keeping the ship's systems operational.")
        print("1. Inspect the core's status.")
        print("2. Attempt to stabilize the reactor.")
        action = input("Enter your choice: ")

        if action == "1":
            print("The core is unstable. It needs immediate repairs.")
        elif action == "2":
            print("Solve the following puzzle to stabilize the reactor:")
            success = reactor_core_puzzle()
            if success:
                print("The reactor is now stable. Ship systems are back online!")
            else:
                print("The reactor remains unstable.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def armory(player):
    while True:
        print("\nThe Armory is secured with heavy doors, and weapons line the walls.")
        print("1. Inspect the locked weapon cabinet.")
        print("2. Search the room for access codes.")
        action = input("Enter your choice: ")

        if action == "1":
            if "Mysterious Key" in player["inventory"]:
                print("You use the Mysterious Key to unlock the cabinet. You obtain a Plasma Rifle!")
                player["inventory"].append("Plasma Rifle")
            else:
                print("The cabinet is locked. You need a key to open it.")
        elif action == "2":
            print("You find a note with strange symbols that might be useful.")
            player["inventory"].append("Access Code Note")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def communications_room(player):
    while True:
        print("\nThe Communications Room is filled with buzzing consoles and a faint whir of static.")
        print("1. Attempt to decode an intercepted signal.")
        print("2. Search for a communications log.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You try to decipher a mysterious alien signal:")
            success = alien_signal_puzzle()
            if success:
                print("You successfully decode the message. It reveals the coordinates of a hidden escape route!")
                player["inventory"].append("Hidden Coordinates")
            else:
                print("You failed to decode the signal. Try again later.")
        elif action == "2":
            print("You find an old communication log detailing a mutiny aboard the ship.")
            player["inventory"].append("Mutiny Log")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def storage_bay(player):
    while True:
        print("\nThe Storage Bay is dimly lit and filled with towering stacks of crates.")
        print("1. Open a crate.")
        print("2. Look for a hidden compartment.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You open a crate and find emergency rations.")
            player["inventory"].append("Emergency Rations")
        elif action == "2":
            if "Mysterious Key" in player["inventory"]:
                print("You find a secret compartment containing advanced tools!")
                player["inventory"].append("Advanced Tools")
            else:
                print("You couldn’t find a way to access the hidden compartment.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def escape_pods(player):
    while True:
        print("\nYou arrive at the Escape Pods. Each pod is sealed and requires an access code to operate.")
        print("1. Inspect the control panel.")
        print("2. Try to use an access code.")
        action = input("Enter your choice: ")

        if action == "1":
            print("The control panel displays an error. You must retrieve the proper access codes.")
        elif action == "2":
            if "Hidden Coordinates" in player["inventory"]:
                print("You input the Hidden Coordinates and successfully unlock a pod!")
                print("Congratulations! You are now ready to escape the ship.")
                return "end_game"
            else:
                print("You don’t have the necessary access codes.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def maintenance_shafts(player):
    while True:
        print("\nThe Maintenance Shafts are dark and filled with twisted pipes and leaking steam.")
        print("1. Proceed cautiously.")
        print("2. Search for a maintenance log.")
        action = input("Enter your choice: ")

        if action == "1":
            print("You carefully navigate the shafts and find a toolbox containing spare parts.")
            player["inventory"].append("Toolbox")
        elif action == "2":
            print("You find a maintenance log detailing prior repairs.")
            player["inventory"].append("Maintenance Log")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")

def alien_containment_unit(player):
    while True:
        print("\nThe Alien Containment Unit hums ominously. Inside, a pulsating orb emits an eerie light.")
        print("1. Approach the containment field.")
        print("2. Attempt to deactivate the containment field.")
        action = input("Enter your choice: ")

        if action == "1":
            print("The orb reacts to your presence. It seems to communicate telepathically.")
        elif action == "2":
            print("Deactivating the field might be dangerous. Solve this puzzle to proceed:")
            success = alien_signal_puzzle()
            if success:
                print("The field deactivates, and the orb transforms into an alien artifact!")
                player["inventory"].append("Alien Artifact")
            else:
                print("You failed to deactivate the field. Try again later.")
        else:
            print("Invalid choice.")
            continue

        next_step = main_action_menu(player)
        if next_step == "move":
            return "room_selector"
        elif next_step == "action_menu":
            continue
        elif next_step == "stay":
            print("You decide to stay and explore more of the room")
