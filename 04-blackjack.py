"""
Blackjack, by Graeme Benson

Inspired by Al Sweigart's "Blackjack" game. Original code can be found at
https://nostarch.com/big-book-small-python-projects
"""

import random
import sys

def main():
    print("""
    Blackjack, by Graeme Benson

    Rules:
        Try to get as close to 21 without going over (busting).
        Kings, Queens, and Jacks are each worth 10 points.
        Aces are worth 1 or 11 points.
        2-10 are worth their face value.
        Hit (H) to take another card.
        Stand (S) to keep your current hand.
        On your first play, you may Double Down (D) to increase your bet, but
        you must Hit exactly one more time before you may Stand.
        In case of a tie, the bet is returned to you, the Player.
        The Dealer stops hitting at 17 or higher.\n\n""")

    money = int(input("Ante up! Enter a number greater than or equal to 1. "))

    # Main game loop
    while True:
        # Validate Player has money to bet with
        if money <= 0:
            print("""
            You're broke...good thing we're not playing with real money.\n
            Thanks for playing!\n""")
            sys.exit()

        # Player enters their bet for this round
        print("Money: ${}".format(money))
        bet = get_bet(money)

        # Give the Player and the Dealer two cards from the deck
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Player actions
        print("Bet: ${}".format(bet))
        # Loop until Player stands or busts
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check whether Player has bust
            if get_hand_value(player_hand) > 21:
                break

            # Get Player's move (Hit, Stand, or Double Down)
            move = get_move(player_hand, money - bet)

            if move == "D":
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print("Your bet has increased to ${}.".format(bet))
                print("Bet: ${}".format(bet))

            if move in ("H", "D"):
                # Hitting or Doubling Down takes another card
                draw_card = deck.pop()
                rank, suit = draw_card
                print("You drew a {} of {}.".format(rank, suit))
                player_hand.append(draw_card)

                if get_hand_value(player_hand) > 21:
                    # Player has busted
                    continue

            if move in ("S", "D"):
                # Standing or Doubling Down stops the Player's turn
                break

        # Dealer's actions
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # Dealer hits
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    # The Dealer has busted
                    break
                input("Press Enter to continue...\n")

        # Show the final hands
        display_hands(player_hand, dealer_hand, True)

        # Get Player and Dealer hand value
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        # Check win conditions
        if dealer_value > 21:
            print("Dealer busts! You win ${}.".format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print("Dealer wins the hand. You lose ${}.".format(bet))
            money -= bet
        elif player_value > dealer_value:
            print("You won the hand! You win ${}.".format(bet))
            money += bet
        elif player_value == dealer_value:
            print("It's a draw. The bet is returned to you.")

        input("Press Enter to continue...\n")

def get_bet(max_bet):
    # Ask the Player how much they will bet this round
    while True:
        print("How much do you bet? ($1-{}, or QUIT)".format(max_bet))
        bet = input(">$ ").upper().strip()

        # Checks if Player quit
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        # Checks whether the Player entered a valid bet
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet

def get_deck():
    # Return a list of rank, suit tuples for all 52 cards
    deck = []

    # Set up the suits
    hearts = chr(9829)
    diamonds = chr(9830)
    spades = chr(9824)
    clubs = chr(9827)
    backside = "backside"

    suits = (hearts, diamonds, spades, clubs)

    for suit in suits:
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for face in ("J", "Q", "K", "A"):
            deck.append((rank, suit))

    # Shuffle and return the deck
    random.shuffle(deck)
    return deck

def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """ Show the Player's and Dealer's cards, hiding the Dealer's first card if
    show_dealer_hand is False"""
    print()

    # Show Dealer's cards
    if show_dealer_hand:
        print("DEALER: ", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")
        display_cards(["backside"] + dealer_hand[1:])

    # Show Player's cards
    print("PLAYER: ", get_hand_value(player_hand))
    display_cards(player_hand)

def get_hand_value(cards):
    """ Returns the value of the cards. Face cards are worth 10 points, Aces are
    worth 1 or 11 points."""
    value = 0
    num_aces = 0

    # Add the value for non-ace cards
    for card in cards:
        rank = card[0]
        if rank == "A":
            num_aces += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)

    # Add the value for aces
    value += num_aces
    for i in range(num_aces):
        # If another 10 points can be added without busting, add it
        if value + 10 <= 21:
            value += 10

    return value

def display_cards(cards):
    """ Display all cards in the card list"""
    rows = ["", "", "", "", ""]

    for c, card in enumerate(cards):
        rows[0] += " ___   " # Prints the top line of the card
        if card == "backside":
            rows[1] += "|## |  "
            rows[2] += "|###|  "
            rows[3] += "|_##|  "
        else:
            rank, suit = card
            rows[1] += "|{} |  ".format(str(rank).ljust(2))
            rows[2] += "| {} |  ".format(suit)
            rows[3] += "|_{}|  ".format(str(rank).rjust(2))

    for row in rows:
        print(row)

def get_move(player_hand, money):
    """ Asks the Player their move, then returns "H" for hit, "S" for stand, and
    "D" for double down."""
    while True:
        # Determines valid moves
        moves = ["(H)it", "(S)tand"]

        # Player can double down on their first move
        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble Down")

        # Get the Player's move
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble Down" in moves:
            return move

if __name__ == "__main__":
    main()
