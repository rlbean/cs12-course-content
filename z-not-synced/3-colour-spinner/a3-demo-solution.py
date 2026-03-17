'''
Name:        Bean (Demo)
Date:        March 2026
Assignment:  Colour Spinner - Teaching Demo
Description: A spinner game that demonstrates random numbers,
             functions with return values, loops, input validation,
             and if/elif/else scoring. This is a TEACHING DEMO —
             not the actual assignment.
'''

import random


# --------------------------------------------------
# spin_wheel()
# Picks a random section (1-4) and returns a colour.
# No parameters — it just generates and returns a result.
# --------------------------------------------------
def spin_wheel():
    section = random.randint(1, 4)
    if section == 1:
        return "Red"
    elif section == 2:
        return "Blue"
    elif section == 3:
        return "Green"
    else:
        return "Yellow"


# --------------------------------------------------
# get_points(colour)
# Receives a colour string. Returns the point value.
# Rarest outcome is checked first.
# --------------------------------------------------
def get_points(colour):
    if colour == "Red":       # rarest — highest points
        return 50
    elif colour == "Blue":
        return 30
    elif colour == "Green":
        return 20
    else:                     # Yellow — most common, lowest points
        return 10


# --------------------------------------------------
# get_num_spins()
# Asks the user how many spins they want (1-8).
# Validates the input. Returns a valid integer.
# --------------------------------------------------
def get_num_spins():
    while True:
        user_input = input("How many spins would you like? (1-8): ")
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= 8:
                return num
        print("  Please enter a whole number between 1 and 8.")


# --------------------------------------------------
# play_game(num_spins)
# Runs the spin loop for the given number of rounds.
# Accumulates and returns the total score.
# --------------------------------------------------
def play_game(num_spins):
    total_score = 0

    for i in range(1, num_spins + 1):
        colour = spin_wheel()                  # get a random colour
        points = get_points(colour)            # look up its point value
        total_score += points                  # add to running total
        print(f"  Spin {i}: {colour} -> {points} pts")

    return total_score                         # send total back to main()


# --------------------------------------------------
# main()
# Controls the overall flow. All final output lives here.
# --------------------------------------------------
def main():
    print("================================")
    print("        COLOUR SPINNER          ")
    print("================================\n")

    num_spins   = get_num_spins()              # get validated input
    print()

    total_score = play_game(num_spins)         # run the game, get score back

    print(f"\n--- Final Score: {total_score} ---")

    if total_score >= 150:
        print("Amazing run - you're on fire!")
    elif total_score >= 80:
        print("Pretty good spin!")
    else:
        print("Better luck next time.")


main()