'''
Name:
Date:
Assignment: Lucky Draw - #3B
Description:
'''

# =============================================================================
# ASSIGNMENT #4 - RANDOM NUMBERS: CHOOSE YOUR THEME
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# OPTION B -  LUCKY DRAW
# ─────────────────────────────────────────────────────────────────────────────
# Draw two cards per round. Cards are 1 (Ace) to 13 (King).
# Scoring (check in order):
#   Both cards = 1 (Aces)  → +100
#   Both cards match        → +50
#   Either card = 2         → -25  (cursed card)
#   Sum > 17                → +20
#   Everything else         → +10
# ─────────────────────────────────────────────────────────────────────────────

import random

# --- OPTION B STARTER CODE ---

def draw_card():
    '''Returns one random card value from 1 (Ace) to 13 (King).'''
    # TODO: return a random number between 1 and 13 (inclusive)
    pass


def calculate_score(card1, card2):
    '''
    Returns the points earned for one round based on the two card values.
    Check conditions in order — stop at the first match.
    '''
    # TODO: add your if/elif/else conditions here
    # Hint: check for double Aces first, then other pairs, then the cursed 2, then sum
    pass


def play_game(rounds):
    '''
    Runs the game for the given number of rounds.
    Returns the final total score.
    '''
    total_score = 0

    # TODO: loop for the number of rounds
    #   - call draw_card() twice to get card1 and card2
    #   - call calculate_score() to get the round score
    #   - add round score to total
    #   - return total when the loop is done

    return total_score


def get_final_message(score):
    '''Returns the final result message as a string based on the score.'''
    # TODO: return the correct message string for the score
    # 200+       → "Card Shark! You read the deck perfectly."
    # 100 - 199  → "Decent hand. Not bad for a draw."
    # below 100  → "The deck was not in your favour today."
    pass


def main():
    '''Main function — handles all user input and all printed output.'''
    print("=" * 40)
    print("  Welcome to Lucky Draw!".center(40))
    print("=" * 40)

    # TODO: ask the user how many rounds they want to play (1-10)
    # TODO: validate the input - keep asking until it's a valid number

    # TODO: call play_game() with the number of rounds
    # TODO: call get_final_message() with the score
    # TODO: print the total score and the final message

    # --- EXTENSION ---
    # Track which round had the best score and which had the worst.
    # Display both at the end, along with the round number.


main()