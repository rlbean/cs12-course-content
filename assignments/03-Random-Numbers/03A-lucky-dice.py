'''
Name:
Date:
Assignment: Lucky Dice Game Show - #3A
Description:
'''

# =============================================================================
# ASSIGNMENT #4 - RANDOM NUMBERS: CHOOSE YOUR THEME
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# OPTION A -  THE LUCKY DICE GAME SHOW
# ─────────────────────────────────────────────────────────────────────────────
# Roll two six-sided dice each round and score points based on what you roll.
# Scoring (check in order):
#   Both dice = 6          → +100
#   Both dice match        → +50
#   Either die = 1         → -25
#   Sum is even            → +20
#   Everything else        → +10
# ─────────────────────────────────────────────────────────────────────────────

import random

# --- OPTION A STARTER CODE ---

def roll_die():
    '''Returns one random integer from 1 to 6.'''
    # TODO: return a random number between 1 and 6 (inclusive)
    pass


def calculate_score(die1, die2):
    '''
    Returns the points earned for one round based on the two dice values.
    Check conditions in order — stop at the first match.
    '''
    # TODO: add your if/elif/else conditions here
    # Hint: check for double 6 first, then other pairs, then individual dice, then sum
    pass


def play_game(rounds):
    '''
    Runs the game for the given number of rounds.
    Returns the final total score.
    '''
    total_score = 0

    # TODO: loop for the number of rounds
    #   - call roll_die() twice to get die1 and die2
    #   - call calculate_score() to get the round score
    #   - add round score to total
    #   - return total when the loop is done

    return total_score


def get_final_message(score):
    '''Returns the final result message as a string based on the score.'''
    # TODO: return the correct message string for the score
    # 200+       → "You're a Lucky Legend!"
    # 100 - 199  → "Not bad! You've got some luck."
    # below 100  → "Better luck next time..."
    pass


def main():
    '''Main function — handles all user input and all printed output.'''
    print("=" * 40)
    print("  Welcome to the Lucky Dice Game Show!".center(40))
    print("=" * 40)

    # TODO: ask the user how many rounds they want to play (1-10)
    # TODO: validate the input — keep asking until it's a valid number

    # TODO: call play_game() with the number of rounds
    # TODO: call get_final_message() with the score
    # TODO: print the total score and the final message

    # --- EXTENSION ---
    # Track which round had the best score and which had the worst.
    # Display both at the end, along with the round number.


main()