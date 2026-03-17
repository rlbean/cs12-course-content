'''
Name:
Date:
Assignment:  Coin Flip Tracker - Teaching Demo
Description:
'''

import random


# --------------------------------------------------
# flip_coin()
# Flips one coin. Returns "Heads" or "Tails".
# --------------------------------------------------
def flip_coin():
    # TODO: Generate a random number between 1 and 2
    # TODO: If it's 1, return "Heads" — otherwise return "Tails"
    pass


# --------------------------------------------------
# get_num_flips()
# Asks the user how many flips (1–10).
# Validates the input and returns a valid integer.
# --------------------------------------------------
def get_num_flips():
    while True:
        user_input = input("How many flips would you like? (1–10): ")

        # TODO: Check that user_input is a digit (use .isdigit())
        # TODO: Convert it to an integer
        # TODO: If it is between 1 and 10 (inclusive), return it
        # TODO: If it fails any check, print a helpful error message

        pass


# --------------------------------------------------
# play_game(num_flips)
# Runs the flip loop for the given number of rounds.
# Counts and returns the total number of Heads.
# --------------------------------------------------
def play_game(num_flips):
    heads_count = 0

    # TODO: Use a for loop to repeat num_flips times
    # TODO: Inside the loop, call flip_coin() and store the result
    # TODO: Print each flip result with its round number
    # TODO: If the result is "Heads", add 1 to heads_count

    return heads_count      # this sends the total back to main() — don't remove it


# --------------------------------------------------
# main()
# Controls the overall flow. All print() output lives here.
# --------------------------------------------------
def main():
    print("================================")
    print("      COIN FLIP TRACKER         ")
    print("================================\n")

    # TODO: Call get_num_flips() and store the result
    # TODO: Call play_game() with that number, store the heads count
    # TODO: Calculate tails = total flips - heads
    # TODO: Print the results (heads count, tails count)
    # TODO: Print a final message: who won, or if it's a tie


main()