'''
Name:
Date:
Assignment: Fishing Tournament - #3C
Description:
'''

# =============================================================================
# ASSIGNMENT #4 - RANDOM NUMBERS: CHOOSE YOUR THEME
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# OPTION C -  FISHING TOURNAMENT
# ─────────────────────────────────────────────────────────────────────────────
# Each cast produces a fish size (1–10) and a rarity (1–6, lower = rarer).
# Scoring (check in order):
#   Size = 10 AND Rarity = 1   → +100  (legendary catch)
#   Rarity = 1 (any size)      → +50   (rare species)
#   Size = 1                   → -25   (caught a boot)
#   Size >= 7                  → +20   (big catch)
#   Everything else            → +10
# ─────────────────────────────────────────────────────────────────────────────

import random

# --- OPTION C STARTER CODE ---

def get_fish_size():
    '''Returns one random integer from 1 to 10. Represents the fish size.'''
    # TODO: return a random number between 1 and 10 (inclusive)
    pass


def get_fish_rarity():
    '''
    Returns one random integer from 1 to 6.
    Lower numbers mean a rarer species (1 is rarest).
    '''
    # TODO: return a random number between 1 and 6 (inclusive)
    pass


def calculate_score(size, rarity):
    '''
    Returns the points earned for one cast based on size and rarity.
    Check conditions in order — stop at the first match.
    '''
    # TODO: add your if/elif/else conditions here
    # Hint: check for size=10 AND rarity=1 first (most specific condition)
    pass


def play_game(rounds):
    '''
    Runs the tournament for the given number of casts.
    Returns the final total score.
    '''
    total_score = 0

    # TODO: loop for the number of rounds
    #   - call get_fish_size() to get the size
    #   - call get_fish_rarity() to get the rarity
    #   - call calculate_score() to get the round score
    #   - add round score to total
    #   - return total when the loop is done

    return total_score


def get_final_message(score):
    '''Returns the final result message as a string based on the score.'''
    # TODO: return the correct message string for the score
    # 200+       → "Tournament Champion! The lake bows to you."
    # 100 - 199  → "Solid day on the water. A few good catches."
    # below 100  → "Better luck next time. Maybe try different bait."
    pass


def main():
    '''Main function — handles all user input and all printed output.'''
    print("=" * 40)
    print("  Welcome to the Fishing Tournament!".center(40))
    print("=" * 40)

    # TODO: ask the user how many casts they want to make (1-10)
    # TODO: validate the input — keep asking until it's a valid number

    # TODO: call play_game() with the number of rounds
    # TODO: call get_final_message() with the score
    # TODO: print the total score and the final message

    # --- EXTENSION (optional bonus) ---
    # Track which cast had the best score and which had the worst.
    # Display both at the end, along with the cast number.


main()