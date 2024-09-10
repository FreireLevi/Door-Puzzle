print("You need to find a paper with a password inside the bedroom, to unlock the door and escape")

answer = input("Where do you want to search? (Bed/Wardrobe/Desk) ").lower().strip()
if answer == "bed":
    answer = print("The paper isn't there. Game Over")

elif answer == "wardrobe":
    answer = print("The paper isn't there. Game Over")

elif answer == "desk":
    answer = input("You found the paper! The number sequence is 18504, do you want to use it? (Yes/No) ").lower().strip()
    if answer == "yes":
        answer = input("Insert the combination to unlock the door: ").lower().strip()
        if answer == "18504":
            answer = print("Congratulations, you unlocked the door!")
        else:
            print("Wrong Combination. Game Over")
    elif answer == "no":
        print("You couldn't unlock the door. Game Over")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
