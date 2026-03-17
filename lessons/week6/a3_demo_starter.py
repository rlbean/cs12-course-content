'''
Name:        
Date:        
Assignment:  Colour Spinner - Teaching Demo
Description: 
'''

import random


# --------------------------------------------------
# spin_wheel()
# Picks a random section (1-4) and returns a colour.
# --------------------------------------------------
def spin_wheel():
    # TODO: Generate a random number between 1 and 4
    # TODO: Return "Red" for 1, "Blue" for 2, "Green" for 3, "Yellow" for 4
    pass


# --------------------------------------------------
# get_points(colour)
# Receives a colour string. Returns the point value.
#   Red    -> 50 pts
#   Blue   -> 30 pts
#   Green  -> 20 pts
#   Yellow -> 10 pts
# --------------------------------------------------
def get_points(colour):
    # TODO: Use if/elif/else to return the right point value
    # Hint: put the rarest/highest outcome first
    pass


# --------------------------------------------------
# get_num_spins()
# Asks the user how many spins they want (1-8).
# Validates the input. Returns a valid integer.
# --------------------------------------------------
def get_num_spins():
    while True:
        user_input = input("How many spins would you like? (1-8): ")

        # TODO: Check that user_input is a digit
        # TODO: Convert to int and check it is between 1 and 8
        # TODO: If valid, return it
        # TODO: If invalid, print a helpful error message

        pass


# --------------------------------------------------
# play_game(num_spins)
# Runs the spin loop for the given number of rounds.
# Accumulates and returns the total score.
# --------------------------------------------------
def play_game(num_spins):
    total_score = 0

    # TODO: Use a for loop to repeat num_spins times
    # TODO: Call spin_wheel() and store the colour
    # TODO: Call get_points() with that colour and store the points
    # TODO: Add points to total_score
    # TODO: Print each round: spin number, colour, and points

    return total_score      # sends the total back to main() — don't remove this


# --------------------------------------------------
# main()
# Controls the overall flow. All final output lives here.
# --------------------------------------------------
def main():
    print("================================")
    print("        COLOUR SPINNER          ")
    print("================================\n")

    # TODO: Call get_num_spins() and store the result
    # TODO: Call play_game() with that number and store the score
    # TODO: Print the final score
    # TODO: Print a final message based on the score:
    #         150+  -> "Amazing run - you're on fire!"
    #         80-149 -> "Pretty good spin!"
    #         below 80 -> "Better luck next time."


main()