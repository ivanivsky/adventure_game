
import random
import time

def intro_text():
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(2)
    enemy_list = ["gorgon", "dragon", "wicked fairie"]
    enemy = random.choice(enemy_list)

    print(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print("In your hand you hold your trusty (but not very effective) dagger.\n")
    time.sleep(2)

def choice_knock_or_cave():
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    print("What would you like to do?")
    time.sleep(2)
    decision_knock_or_cave = input("(Please enter 1 or 2.)\n")

    if decision_knock_or_cave == 1:
        def knock_dagger()
        print("knock")
    elif decision_knock_or_cave == 2:
        def cave_dagger()
        print("cave")
    else:
        input("What would like to do?")

def cave_dagger():
    print("cave")

def knock_dagger():
    print("You approach the door of the house.")
    print("You are about to knock when the door opens and out steps a gorgon.")
    print("Eep! This is the gorgon's house!")
    print("The gorgon attacks you!")
    print("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    input("Would you like to (1) fight or (2) run away?")

intro_text()
choice_knock_or_cave()
