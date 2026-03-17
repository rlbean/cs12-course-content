'''
Name:
Date:
Assignment: Monster Battle - #3D
Description:
'''

# =============================================================================
# ASSIGNMENT #4 - RANDOM NUMBERS: CHOOSE YOUR THEME
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# OPTION D - MONSTER BATTLE
# ─────────────────────────────────────────────────────────────────────────────
# Each round, you and the monster both roll an attack die (1–6).
# Scoring (check in order):
#   Player = 6 AND Monster = 1   → +100  (perfect strike)
#   Player = Monster             → +50   (clash)
#   Player = 1                   → -25   (critical miss)
#   Player > Monster             → +20   (you win the round)
#   Player < Monster             → +10   (monster wins the round)
# ─────────────────────────────────────────────────────────────────────────────

import random

# --- OPTION D STARTER CODE ---

def roll_attack():
    '''
    Returns one random attack value from 1 to 6.
    Call this once for the player and once for the monster each round.
    '''
    # TODO: return a random number between 1 and 6 (inclusive)
    pass


def calculate_score(player, monster):
    '''
    Returns the points earned for one battle based on player vs. monster rolls.
    Check conditions in order — stop at the first match.
    '''
    # TODO: add your if/elif/else conditions here
    # Hint: check for perfect strike first (most specific condition)
    pass


def play_game(rounds):
    '''
    Runs the battle for the given number of rounds.
    Returns the final total score.
    '''
    total_score = 0

    # TODO: loop for the number of rounds
    #   - call roll_attack() for the player
    #   - call roll_attack() for the monster
    #   - call calculate_score() to get the round score
    #   - add round score to total
    #   - return total when the loop is done

    return total_score


def get_final_message(score):
    '''Returns the final result message as a string based on the score.'''
    # TODO: return the correct message string for the score
    # 200+       → "Legendary Warrior! No monster can stop you."
    # 100 - 199  → "Solid fighter. You held your own out there."
    # below 100  → "The monsters got the better of you today."
    pass


def main():
    '''Main function — handles all user input and all printed output.'''
    print("=" * 40)
    print("  Welcome to Monster Battle!".center(40))
    print("=" * 40)

    # TODO: ask the user how many battles they want to fight (1-10)
    # TODO: validate the input — keep asking until it's a valid number

    # TODO: call play_game() with the number of rounds
    # TODO: call get_final_message() with the score
    # TODO: print the total score and the final message

    # --- EXTENSION ---
    # Track which battle had the best score and which had the worst.
    # Display both at the end, along with the round number.


main()