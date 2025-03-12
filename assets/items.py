def use_item(player, item):
    if item in player["inventory"]:
        if item == "Medkit":
            print("You use the Medkit and regain 50 health.")
            player["health"] += 50
            player["inventory"].remove(item)
        else:
            print(f"You use the {item}.")
            player["inventory"].remove(item)
    else:
        print(f"You don't have a {item}.")
