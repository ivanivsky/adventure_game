

import random
import time


def print_pause(sentence):
    print(sentence)
    time.sleep(2)


def intro_text():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")

    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")

    item = "dagger"
    option_knock_or_cave_generic(item)


def option_knock_or_cave_generic(item):
    item = item
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    decision_knock_or_cave_generic(item)


def decision_knock_or_cave_generic(item):

    item = item
    decision = None

    while decision != "1" and decision != "2":
        decision = input("(Please enter 1 or 2.)\n")

        if item == "dagger" and decision == "1":
            knock_dagger()
        elif item == "dagger" and decision == "2":
            cave_dagger()
        elif item == "sword" and decision == "1":
            knock_sword()
        elif item == "sword" and decision == "2":
            cave_sword()
        else:
            True


def cave_dagger():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger "
                "and take the sword with you.")
    print_pause("You walk back out to the field.\n")

    item = "sword"

    option_knock_or_cave_generic(item)


def cave_sword():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff. "
                "It's just an empty cave now.\n")

    item = "sword"
    option_knock_or_cave_generic(item)


# def cave_decision(item):
#     print_pause("You walk back out to the field.\n")
#     print_pause("Enter 1 to knock on the door of the house.")
#     print_pause("Enter 2 to peer into the cave.")
#     print_pause("What would you like to do?")
#     decision_sword = input("(Please enter 1 or 2.)\n")
#
#     if item == "dagger":
#         cave_dagger()
#     elif item == "sword":
#         cave_sword()
#     else:
#         print("what is going on?")


def knock_dagger():

    item = "dagger"

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                f"out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this, what with "
                "only having a tiny dagger.")

    option_fight_or_flight_generic(item)


def knock_sword():

    item = "sword"

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")

    option_fight_or_flight_generic(item)


def option_fight_or_flight_generic(item):
    item = item
    fight_or_flight = ""

    while fight_or_flight != "1" and fight_or_flight != "2":
        fight_or_flight = input("Would you like to (1) fight or (2) "
                                    "run away?\n")

        if fight_or_flight == "1" and item == "dagger":
            fight_dagger()
        elif fight_or_flight == "2":
            flee_generic(item)
        elif fight_or_flight == "1" and item == "sword":
            fight_sword()
        else:
            True


def fight_dagger():
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {enemy}.")
    print_pause("You have been defeated!")

    play_again()


def flee_generic(item):
    item = item
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n")
    option_knock_or_cave_generic(item)


def flee_dagger():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n")

    item = "dagger"

    option_knock_or_cave_generic(item)


def fight_sword():
    print_pause(f"As the {enemy} moves to attack, "
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand "
                "as you brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your shiny "
                "new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")

    play_again()


def flee_sword():
    print("shouldn't get here")


def play_again():

    play = ""
    while play != "y" and play != "n":
        play = input("Would you like to play again? (y/n)\n").lower()

        if play != "y" and play != "n":
            play_again()

        if play == "y":
            print("Excellent! Restarting the game ...")
            intro_text()
        elif play == "n":
            print("Thanks for playing! See you next time.")
        else:
            True

#def game_restart():


enemy_list = ["gorgon", "dragon", "wicked fairie", "pirate"]
enemy = random.choice(enemy_list)


def main():
    intro_text()
    option_knock_or_cave_dagger()


if __name__ == "__main__":
    main()
