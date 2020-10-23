

import random
import time

def enemy_generation():
    enemy_list = ["gorgon", "dragon", "wicked fairie", "pirate"]
    enemy = random.choice(enemy_list)
    return enemy

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
    put_knock_or_cave_options(item)


def put_knock_or_cave_options(item):
    item = item
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    get_knock_or_cave_decision(item)


def get_knock_or_cave_decision(item):

    item = item

    prompt = "(Please enter 1 or 2.)\n"

    options = ["1", "2"]

    choice = validate_input(prompt, options)

    if item == "dagger" and choice == "1":
        knock_dagger()
    elif item == "dagger" and choice == "2":
        cave_dagger()
    elif item == "sword" and choice == "1":
        knock_sword()
    elif item == "sword" and choice == "2":
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

    _knock_or_cave_options(item)


def cave_sword():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff. "
                "It's just an empty cave now.\n")

    item = "sword"
    put_knock_or_cave_options(item)


def knock_dagger():

    item = "dagger"

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                f"out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this, what with "
                "only having a tiny dagger.")

    put_fight_or_flight_options(item)


def knock_sword():

    item = "sword"

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")

    put_fight_or_flight_options(item)


def put_fight_or_flight_options(item):
    item = item

    prompt = "Would you like to (1) fight or (2) run away?\n"

    options = ["1", "2"]

    choice = validate_input(prompt, options)

    if choice == "1" and item == "dagger":
        fight_dagger()
    elif choice == "2":
        flee_generic(item)
    elif choice == "1" and item == "sword":
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

    put_knock_or_cave_options(item)


def flee_dagger():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.\n")

    item = "dagger"

    put_knock_or_cave_options(item)


def fight_sword():
    print_pause(f"As the {enemy} moves to attack, "
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand "
                "as you brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your shiny "
                "new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")

    play_again()


def validate_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option == response:
                return response


def play_again():
    prompt = "Would you like to play again? (y/n)\n"

    options = ["y", "n"]

    choice = validate_input(prompt, options)

    if choice == "y":
        print_pause("Excellent! Restarting the game ...")
        intro_text()
    elif choice == "n":
        exit_game()


def exit_game():
        print_pause("Thanks for playing! See you next time.")
        quit()


enemy = enemy_generation()
intro_text()

#def main():


if __name__ == "__main__":
    main()
