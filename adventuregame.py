
import random
import time

def intro_text():
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(2)

    print(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print("In your hand you hold your trusty (but not very effective) dagger.\n")
    time.sleep(2)

    item = "dagger"
    option_knock_or_cave_generic(item)

def option_knock_or_cave_generic(item):
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    print("What would you like to do?")
    time.sleep(2)
    decision_knock_or_cave = int(input("(Please enter 1 or 2.)\n"))

def option_knock_or_cave_dagger():
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    print("What would you like to do?")
    time.sleep(2)
    decision_knock_or_cave = int(input("(Please enter 1 or 2.)\n"))

    decision_knock_or_cave_generic(decision_knock_or_cave)

def decision_knock_or_cave_generic(decision_knock_or_cave):
    if decision_knock_or_cave == 1:
        knock_dagger()
        print("knock")
    elif decision_knock_or_cave == 2:
        cave_dagger()
        print("cave")
    else:
        input("What would like to do?")
        # need to return to the options

def cave_dagger():
    print("You peer cautiously into the cave.")
    time.sleep(2)
    print("It turns out to be only a very small cave.")
    time.sleep(2)
    print("Your eye catches a glint of metal behind a rock.")
    time.sleep(2)
    print("You have found the magical Sword of Ogoroth!")
    time.sleep(2)
    print("You discard your silly old dagger and take the sword with you.")
    time.sleep(2)

    item = "sword"

    cave_decision(item)

def cave_sword():
    print("You peer cautiously into the cave.")
    print("You've been here before, and gotten all the good stuff. It's just an empty cave now.")

    item = "sword"
    cave_decision(item)


def cave_decision(item):
    print("You walk back out to the field.\n")
    time.sleep(2)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to peer into the cave.")
    time.sleep(2)
    print("What would you like to do?")
    time.sleep(2)
    decision_sword = input("(Please enter 1 or 2.)\n")

    if item == "dagger":
        cave_dagger()
    elif item == "sword":
        cave_sword()
    else:
        print("what is going on?")

def knock_dagger():
    print("You approach the door of the house.")
    time.sleep(2)
    print(f"You are about to knock when the door opens and out steps a {enemy}.")
    time.sleep(2)
    print(f"Eep! This is the {enemy}'s house!")
    time.sleep(2)
    print(f"The {enemy} attacks you!")
    time.sleep(2)
    print("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    time.sleep(2)

    option_fight_or_flight_dagger()

def option_knock_or_cave_sword():
    print("hey girl")

def option_fight_or_flight_dagger():
    fight_flight_dagger = int(input("Would you like to (1) fight or (2) run away?\n"))
    if fight_flight_dagger == 1:
        fight_dagger()
    elif fight_flight_dagger == 2:
        flee_dagger()
    else:
        input("What would you like to do?")
        # need to do something here

def fight_dagger():
    print("You do your best...")
    time.sleep(2)
    print(f"but your dagger is no match for the {enemy}.")
    time.sleep(2)
    print("You have been defeated!")
    play_again = input("Would you like to play again? (y/n)")

    if play_again == "y":
        print("Excellent! Restarting the game ...")
        intro_text()
    elif play_again == "n":
        print("Thanks for playing! See you next time.")
        # terminate the whole program somehow.
    else:
        input("What would you like to do?")
        # needs to do something.


def flee_dagger():
    print("You run back into the field. Luckily, you don't seem to have been followed.\n")
    time.sleep(2)

    option_knock_or_cave_dagger()


#def game_restart():

enemy_list = ["gorgon", "dragon", "wicked fairie"]
enemy = random.choice(enemy_list)

def main():
    intro_text()
    option_knock_or_cave_dagger()

if __name__ == "__main__":
    main()
