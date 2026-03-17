'''
Name:
Date:
Assignment: #4 - The Helper Hub
Description:
'''

import random


# ──────────────────────────────────────────────────────────────────────────────
# show_menu
# Purpose  : Displays the Helper Hub menu and collects the user's choice.
# Params   : None
# Returns  : The user's validated choice as an integer (1–5)
# ──────────────────────────────────────────────────────────────────────────────
def show_menu():
    print()
    print("╔══════════════════════════════════╗")
    print("║       🛠  The Helper Hub         ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Tip Calculator               ║")
    print("║  2. Dice Roller                  ║")
    print("║  3. Temperature Converter        ║")
    print("║  4. Coin Flipper                 ║")
    print("║  5. Exit                         ║")
    print("╚══════════════════════════════════╝")

    choice = 0
    while choice < 1 or choice > 5:
        try:
            # TODO: ask the user to enter a number between 1 and 5
            # TODO: store it in the choice variable above
            # HINT: int(input("..."))
            pass
        except ValueError:
            print("  Please enter a number.")
    return choice


# ──────────────────────────────────────────────────────────────────────────────
# calculate_tip
# Purpose  : Calculates the tip amount and the total bill.
# Params   : bill        (float) — the pre-tip bill amount
#            tip_percent (float) — tip percentage, e.g. 18.0 means 18%
# Returns  : A tuple (tip_amount, total) — both floats
# ──────────────────────────────────────────────────────────────────────────────
def calculate_tip(bill, tip_percent):
    # TODO: calculate tip_amount  (bill multiplied by tip_percent divided by 100)
    tip_amount = 0.0

    # TODO: calculate total  (bill plus tip_amount)
    total = 0.0

    return tip_amount, total        # returning TWO values back to main()


# ──────────────────────────────────────────────────────────────────────────────
# roll_die
# Purpose  : Simulates one die roll.
# Params   : sides (int) — number of sides on the die
# Returns  : A random integer from 1 to sides (inclusive)
# ──────────────────────────────────────────────────────────────────────────────
def roll_die(sides):
    # TODO: return a random integer between 1 and sides
    # HINT: random.randint(low, high)
    pass


# ──────────────────────────────────────────────────────────────────────────────
# roll_dice
# Purpose  : Rolls multiple dice by calling roll_die() once per die.
# Params   : num_dice (int) — how many dice to roll
#            sides    (int) — how many sides each die has
# Returns  : A list of integer results, one per die
# ──────────────────────────────────────────────────────────────────────────────
def roll_dice(num_dice, sides):
    results = []

    # TODO: loop num_dice times
    #       each time, call roll_die(sides) and append the result to results

    return results


# ──────────────────────────────────────────────────────────────────────────────
# convert_temp
# Purpose  : Converts a temperature between Celsius and Fahrenheit.
# Params   : value     (float) — the temperature to convert
#            direction (str)   — "C" converts Celsius to Fahrenheit
#                                "F" converts Fahrenheit to Celsius
# Returns  : The converted temperature as a float
# ──────────────────────────────────────────────────────────────────────────────
def convert_temp(value, direction):
    converted = 0.0

    if direction == "C":
        # TODO: apply the C→F formula: (value * 9/5) + 32
        pass
    elif direction == "F":
        # TODO: apply the F→C formula: (value - 32) * 5/9
        pass

    return converted


# ──────────────────────────────────────────────────────────────────────────────
# flip_coin
# Purpose  : Simulates flipping a coin by calling roll_die(2).
# Params   : num_flips (int) — how many times to flip
# Returns  : A tuple (heads_count, tails_count)
# Note     : roll_die(2) returning 1 = Heads, 2 = Tails
# ──────────────────────────────────────────────────────────────────────────────
def flip_coin(num_flips):
    heads = 0
    tails = 0

    # TODO: loop num_flips times
    #       each time call roll_die(2) to get 1 (Heads) or 2 (Tails)
    #       update heads or tails count accordingly

    return heads, tails


# ──────────────────────────────────────────────────────────────────────────────
# exit_program
# Purpose  : Prints a farewell message.
# Params   : None
# Returns  : Nothing
# ──────────────────────────────────────────────────────────────────────────────
def exit_program():
    print("\nThanks for using the Helper Hub. See you next time!")


# ──────────────────────────────────────────────────────────────────────────────
# main
# Purpose  : Runs the menu loop and routes each choice to the right function.
# ──────────────────────────────────────────────────────────────────────────────
def main():
    print("Welcome to the Helper Hub!")

    while True:
        choice = show_menu()        # show_menu RETURNS the choice to us here

        if choice == 1:
            # --- Tip Calculator ---
            bill = float(input("  Enter the bill amount: $"))
            pct  = float(input("  Enter tip percentage (e.g. 18): "))

            # TODO: call calculate_tip(bill, pct)
            # TODO: store the two returned values like this:
            #       tip, total = calculate_tip(bill, pct)
            # TODO: print tip and total with $ signs and 2 decimal places

        elif choice == 2:
            # --- Dice Roller ---
            num   = int(input("  How many dice? "))
            sides = int(input("  How many sides per die? "))

            # TODO: call roll_dice(num, sides) and store the returned list
            # TODO: print the list of rolls
            # TODO: print their sum using sum()

        elif choice == 3:
            # --- Temperature Converter ---
            val       = float(input("  Enter temperature: "))
            direction = input("  Convert from C or F? ").strip().upper()

            # TODO: call convert_temp(val, direction) and store the result
            # TODO: print the converted temperature with the correct unit label

        elif choice == 4:
            # --- Coin Flipper ---
            flips = int(input("  How many times to flip? "))

            # TODO: call flip_coin(flips) and store the returned tuple
            # TODO: print heads and tails counts

        elif choice == 5:
            exit_program()
            break                   # exits the while True loop — program ends here


main()