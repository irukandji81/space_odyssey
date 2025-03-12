def hacking_puzzle():
    print("\nYou approach a locked door. The panel displays a code challenge:")
    print("Decode this sequence: 2, 4, 8, 16, ?")
    answer = input("Enter your answer: ")
    
    if answer == "32":
        print("Access granted! The door opens.")
        return True
    else:
        print("Access denied. The alarm starts blaring!")
        return False

def reactor_core_puzzle():
    print("\nThe Reactor Core is malfunctioning. To stabilize it, solve this sequence:")
    print("Which number comes next? 3, 6, 9, 12, ?")
    answer = input("Enter your answer: ")
    if answer == "15":
        print("The reactor stabilizes! Power is restored.")
        return True
    else:
        print("Incorrect! The reactor remains unstable.")
        return False

def alien_signal_puzzle():
    print("\nYou intercept an alien signal. Solve the following code to understand it:")
    print("Decode this: A=1, B=2, C=3. What is '8-1-12-9-5-14'?")
    answer = input("Enter your answer: ")
    if answer.lower() == "alien":
        print("You deciphered the signal! It’s a distress call from an alien species.")
        return True
    else:
        print("You failed to decode the message.")
        return False
