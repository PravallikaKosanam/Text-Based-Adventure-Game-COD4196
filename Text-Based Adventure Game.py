import time

def introduction():
    print("Welcome to Lost in the Forest!")
    print("You find yourself in the middle of a dense forest.")
    print("Your goal is to find your way out safely.\n")

def choose_path():
    print("Which path will you choose?")
    print("1. Follow the river")
    print("2. Venture into the dark cave")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def follow_river():
    print("\nYou decide to follow the river.")
    print("After walking for some time, you spot a bridge.")
    print("Do you want to cross the bridge?")
    bridge_choice = input("Yes or No: ").lower()
    if bridge_choice == "yes":
        print("\nYou successfully cross the bridge and continue your journey.")
        time.sleep(2)
        print("\nAfter crossing the bridge, you find a road in the middle of the dark forest.")
        print("The road has two directions: left and right.")
        road_choice = input("Which direction will you choose? Left or Right: ").lower()
        if road_choice == "left":
            print("\nYou choose to go left and follow the road.")
            print("After walking for a while, you reach a highway.")
            print("\nCongratulations! You have navigated through the dark forest.")
            print("You successfully completed your adventure!")
        elif road_choice == "right":
            print("\nYou choose to go right and encounter a cruel animal in a cave!")
            animal_choice = input("Do you want to kill it or escape? Kill or Escape: ").lower()
            if animal_choice == "kill":
                print("\nYou bravely fight and manage to kill the animal.")
                print("After defeating the animal, you find a path that leads to a nearby village.")
                print("\nCongratulations! You have safely navigated from the dark forest.")
            else:
                print("\nYou try to escape, but the animal catches you.")
                print("Game Over! You've been killed by the animal.")
                print("You can try again or leave.")
        else:
            print("\nInvalid choice. Please enter Left or Right.")
            follow_river()  # Restart the river path
    else:
        print("\nYou decide not to cross the bridge.")
        print("You continue walking along the riverbank.")

def dark_cave():
    print("\nYou bravely enter the dark cave.")
    print("It's pitch black inside.")
    print("You can barely see anything.")
    time.sleep(2)
    print("\nSuddenly, you hear a growling noise.")
    print("Do you want to proceed forward or retreat?")
    cave_choice = input("Proceed or Retreat: ").lower()
    if cave_choice == "proceed":
        print("\nYou cautiously move forward, but the growling gets louder.")
        print("You realize there's a bear in the cave!")
        print("You run out of the cave as fast as you can!")
    else:
        print("\nYou decide it's too risky and retreat from the cave.")

def main():
    introduction()
    choice = choose_path()
    if choice == "1":
        follow_river()
    elif choice == "2":
        dark_cave()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
