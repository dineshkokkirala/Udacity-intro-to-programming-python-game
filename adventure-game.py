import random
import time


def introduction(i, opt):
    toPrint("You find yourself standing in an open ground, filled "
            "with grass and green flowers.\n")
    toPrint("Rumor has it that a " + opt + " is somewhere around "
            "here, and has been terrifying the nearby village.\n")
    toPrint("In front of you is a house.\n")
    toPrint("To your right is a jungle.\n")
    toPrint("In your hand you hold only your book\n")


def toPrint(message):
    print(message)
    time.sleep(3)


def house(i, opt):
    toPrint("\nYou approach the door of the house.")
    toPrint("\nYou are about to knock when the door "
            "opens and out steps a " + opt + ".")
    toPrint("\nYeah! This is the " + opt + "'s house!")
    toPrint("\nThe " + opt + " attacks you!\n")
    if "sward" not in i:
        toPrint("You feel a bit under-prepared for this, "
                "what with only having a dagger.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sward" in i:
                toPrint("\nAs the " + opt + " moves to attack, "
                        "you unsheath your new sword.")
                toPrint("\nThe Sword of Ogoroth shines brightly in "
                        "your hand as you brace yourself for the "
                        "attack.")
                toPrint("\nBut the " + opt + "takes one look at "
                        "your shiny new toy and runs away!")
                toPrint("\nYou have rid the town of the " + opt +
                        ". You are victorious!\n")
            else:
                toPrint("\nYou do your best...")
                toPrint("but your dagger is no match for the "
                        + opt + ".")
                toPrint("\nYou have been defeated!\n")
            again()
            break
        if choice2 == "2":
            toPrint("\nYou run back into the ground. "
                    "\nLuckily, you don't seem to have been "
                    "followed.\n")
            ground(i, opt)
            break


def jungle(i, opt):
    if "sward" in i:
        toPrint("\nYou peer cautiously into the jungle.")
        toPrint("\nYou've been here before, and gotten all"
                " the good stuff. It's just an empty jungle"
                " now.")
        toPrint("\nYou walk back to the ground.\n")
    else:
        toPrint("\nYou peer cautiously into the jungle.")
        toPrint("\nIt turns out to be only a very small jungle.")
        toPrint("\nYour eye catches a glint of metal behind a "
                "rock.")
        toPrint("\nYou have found the magical Sword")
        toPrint("\nYou discard your silly old dagger and take "
                "the sword with you.")
        toPrint("\nYou walk back out to the ground.\n")
        i.append("sward")
    ground(i, opt)


def ground(i, opt):
    toPrint("Enter 1 to knock on the door of the house.")
    toPrint("Enter 2 to peer into the jungle.")
    toPrint("What would you like to do?")
    while True:
        opt1 = input("(Please enter 1 or 2.)\n")
        if opt1 == "1":
            house(i, opt)
            break
        elif opt1 == "2":
            jungle(i, opt)
            break


def again():
    again = input("Would you like to play again this game? (Y/N)").lower()
    if again == "y":
        toPrint("\n\nExcellent! Restarting the game ...\n\n")
        play()
    elif again == "n":
        toPrint("\n\nThanks for playing!\n\n")
    else:
        again()


def play():
    i = []
    opt = random.choice(["tiger", "lion", "snake", "dragon"])
    introduction(i, opt)
    ground(i, opt)


play()
