'''
Name:
Date:
Assignment: The Helper Hub - #4A
Description:
'''

# =============================================================================
# ASSIGNMENT #5 — MULTIPLE METHODS: CHOOSE YOUR THEME
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# OPTION A -  THE HELPER HUB
# ─────────────────────────────────────────────────────────────────────────────
# A menu-driven utility with 4 tools + exit.
#
# Menu:
#   1 - Tip Calculator       → calculate_tip(bill, tip_percent) → tuple
#   2 - Dice Roller          → roll_dice(num_dice, sides)       → list
#   3 - Temperature Converter→ convert_temp(value, direction)   → float
#   4 - Coin Flipper         → flip_coin(num_flips)             → tuple
#   5 - Exit
#
# Shared primitive: roll_die(sides) — called by roll_dice() and flip_coin()
# ─────────────────────────────────────────────────────────────────────────────

import random


def roll_die(sides):
    '''
    Returns one random integer from 1 to sides (inclusive).
    This is a shared utility — called by roll_dice() and flip_coin().
    It never prints anything.

    Parameters: sides (int) — the number of sides on the die
    Returns: int
    '''
    # TODO: return a random number from 1 to sides
    pass


def calculate_tip(bill, tip_percent):
    '''
    Calculates the tip amount and the total bill.
    Does NOT print — returns both values as a tuple.

    Parameters: bill (float), tip_percent (float)
    Returns: tuple (tip_amount, total)
    '''
    # TODO: calculate the tip amount
    # TODO: calculate the total (bill + tip)
    # TODO: return tip_amount, total
    pass


def roll_dice(num_dice, sides):
    '''
    Rolls a given number of dice, each with the given number of sides.
    Calls roll_die() once per die and collects the results.
    Does NOT print — returns the list of rolls.

    Parameters: num_dice (int), sides (int)
    Returns: list of ints
    '''
    rolls = []
    # TODO: loop num_dice times, call roll_die(sides) each time, append to rolls
    return rolls


def convert_temp(value, direction):
    '''
    Converts a temperature between Celsius and Fahrenheit.
    Does NOT print — returns the converted value.

    Parameters:
        value (float)     — the temperature to convert
        direction (str)   — "C" to convert Celsius→Fahrenheit
                            "F" to convert Fahrenheit→Celsius
    Returns: float

    Formulas:
        C → F: (value × 9/5) + 32
        F → C: (value - 32) × 5/9
    '''
    # TODO: check direction and apply the correct formula
    # TODO: return the converted temperature
    pass


def flip_coin(num_flips):
    '''
    Simulates flipping a coin a given number of times.
    Uses roll_die(2) for each flip: 1 = Heads, 2 = Tails.
    Does NOT print — returns counts as a tuple.

    Parameters: num_flips (int)
    Returns: tuple (heads_count, tails_count)
    '''
    heads = 0
    tails = 0
    # TODO: loop num_flips times
    #   - call roll_die(2) for each flip
    #   - increment heads or tails based on the result
    return heads, tails


def show_menu():
    '''
    Displays the Helper Hub menu and returns the user's validated choice.
    Keeps asking until a valid integer between 1 and 5 is entered.

    Returns: int (1–5)
    '''
    print()
    print("----------------------------------")
    print("---- The Helper Hub ----")
    print("----------------------------------")
    print("    - 1 -  Tip Calculator")
    print("    - 2 -  Dice Roller")
    print("    - 3 -  Temperature Converter")
    print("    - 4 -  Coin Flipper")
    print("    - 5 -  Exit")
    print("----------------------------------")

    # TODO: get and validate the user's choice (must be 1–5)
    # TODO: return the validated integer choice
    pass


def exit_program():
    '''Prints a farewell message. Called by main() before break.'''
    print("Thanks for using the Helper Hub. Goodbye!")


def main():
    '''
    Entry point. Contains the while True menu loop.
    Handles all user input and all printed output.
    Calls show_menu() to get the choice, then routes to the correct tool.
    Uses break to exit when the user chooses 5.
    '''
    while True:
        choice = show_menu()

        if choice == 1:
            # Tip Calculator
            # TODO: get bill amount and tip percentage from the user
            # TODO: call calculate_tip(bill, tip_percent)
            # TODO: print the tip amount and total, formatted with $ and 2 decimal places
            pass

        elif choice == 2:
            # Dice Roller
            # TODO: ask how many dice and how many sides
            # TODO: call roll_dice(num_dice, sides)
            # TODO: print the individual rolls and their sum
            pass

        elif choice == 3:
            # Temperature Converter
            # TODO: ask for the temperature value
            # TODO: ask for the direction ("C" or "F") and validate it
            # TODO: call convert_temp(value, direction)
            # TODO: print the result with the correct unit label
            pass

        elif choice == 4:
            # Coin Flipper
            # TODO: ask how many times to flip
            # TODO: call flip_coin(num_flips)
            # TODO: print the heads and tails counts
            pass

        elif choice == 5:
            exit_program()
            break

        # --- EXTENSION ---
        # Add an elif choice == 6 block for your custom tool.
        # Your tool must accept at least 1 parameter, return a value,
        # and call at least one existing function in this program.


main()