"""
Cold-Warm-Hot, a deductive logic game.

Inspired by Al Sweigart's "Bagels" game. Original code can be found at
https://nostarch.com/big-book-small-python-projects
"""
import random

num_digits = 3
max_guesses = 10

def main():
    print("""Cold-Warm-Hot, a deductive logic game. \n
    by Graeme Benson \n
    I am thinking of a {}-digit number with no repeated digits. \n
    Try to guess what it is. Hints: \n
    Cold: No correct digit
    Warm: One correct, but misplaced digit
    Hot: One correct, properly placed digit
    \n
    Example: If the number I have thought of is 123 and your guess was 135, the
    hints would be Hot Warm.
    """.format(num_digits))

    while True: # Main loop
        # Define and store "thought-up" number
        secret = get_secret()
        print("I have thought of a number. You have {} guesses to figure out what it is.".format(max_guesses))

        guess_count = 1
        while guess_count <= max_guesses:
            guess = ""
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess #{}".format(guess_count))
                guess = input("> ")

            clues = get_clues(guess, secret)
            print(clues)
            guess_count += 1

            if guess == secret:
                break
            if guess_count > max_guesses:
                print("You ran out of guesses. The correct answer was {}.".format(secret))

        print("Would you like to play again? (Yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing! Have a great life!")

def get_secret():
    """Returns a string made up of num_digits which are random and unique."""
    n = list('0123456789')
    random.shuffle(n)
    secret = ""
    for i in range(num_digits):
        secret += str(n[i])
    return secret

def get_clues(guess, secret):
    """Returns a string with the clues for a guess"""
    if guess == secret:
        return "Correct! You've won!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            # A correct digit is in the correct place
            clues.append("Hot")
        elif guess[i] in secret:
            # A correct digit is in the incorrect place
            clues.append("Warm")
    if len(clues) == 0:
        # No correct digits
        return "Cold"
    else:
        # Sort the clue order so it doesn't give away the answer
        clues.sort()
        return " ".join(clues)

if __name__ == "__main__":
    main()
