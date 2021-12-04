"""
Dice Roller, by Graeme Benson

Original code can be found at
https://nostarch.com/big-book-small-python-projects
"""
import random
import sys

print("""Dice Roller, by Graeme Benson
Enter the type and number of dice you'd like to roll. The format is:
# of dice (d), followed by the # of sides. You can add a modifier, as well.
Examples:
    One 20-sided die
    1d20

    Two 10-sided dice
    2d10

    Three 6-sided dice with a +2 modifier
    3d6+2

QUIT quits the program.\n""")

# Main program loop
while True:
    try:
        # Prompt for user's roll
        dice_input = input("I roll ")
        if dice_input.upper() == "QUIT":
            print("\nThanks for playing!\n")
            sys.exit()
        dice_string = dice_input.lower().replace(" ", "")

        # Find the d
        d_index = dice_string.find("d")
        if d_index == -1:
            raise Exception("""Missing the "d" character.""")

        # Get number of dice
        num_dice = dice_string[:d_index]
        if not num_dice.isdecimal():
            raise Exception("""Missing the number of dice.""")
        num_dice = int(num_dice)

        # Find if there is a modifier
        positive_mod_index = dice_string.find("+")
        negative_mod_index = dice_string.find("-")
        if positive_mod_index != -1:
            mod_index = positive_mod_index
        elif negative_mod_index != -1:
            mod_index = negative_mod_index
        else:
            mod_index = -1

        # Find the number of sides on the die
        if mod_index == -1:
            num_sides = dice_string[d_index + 1 :]
        else:
            num_sides = dice_string[d_index + 1 : mod_index]
        if not num_sides.isdecimal():
            raise Exception("""Missing number of sides.""")
        num_sides = int(num_sides)

        # Find the modifier amount
        if mod_index == -1:
            mod_amount = 0
        else:
            mod_amount = int(dice_string[mod_index + 1 :])
        if dice_string[mod_index] == "-":
            mod_amount = -mod_amount

        # Simulate rolls
        rolls = []
        for d in range(num_dice):
            roll_result = random.randint(1, num_sides)
            rolls.append(roll_result)

        # Display the total roll
        print("\nYou rolled " + str(sum(rolls) + mod_amount) + "!")

        # Display the individual rolls
        print("Rolls: " + str(rolls) + "\n")

    except Exception as exc:
        # Catch and display any exceptions
        print("""Invalid input. Enter something like "3d6" or "2d8+2".\n
        Input was invalid because: {}""".format(str(exc)))
        continue
