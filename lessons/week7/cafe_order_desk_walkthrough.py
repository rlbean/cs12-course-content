'''
Name:
Date:
Assignment: Assignment 4 Demo - Cafe Order Desk
Description: A menu-driven cafe ordering program that demonstrates
             multiple functions with return values and a while True loop.
'''

import random

# ─────────────────────────────────────────────────────────────
# RULE: Helper functions use RETURN, not print.
#       main() is the ONLY function that prints output.
# ─────────────────────────────────────────────────────────────


def show_menu():
    # Return the menu as a string (do not print here)
    # It should look something like:
    #   === Cafe Order Desk ===
    #   1. Check drink price
    #   2. Calculate order total
    #   3. Check for a discount
    #   4. Exit
    #   Your choice:
    pass


def get_drink_price(choice):
    # Takes the user's drink choice (int)
    # Returns the price (float) for that drink
    # Drinks: 1 = Espresso ($3.50), 2 = Latte ($4.75), 3 = Specialty ($5.25)
    # If the choice is invalid, return 0.0
    pass


def calculate_total(price, quantity):
    # Takes a price (float) and a quantity (int)
    # Returns the total cost (float) - price × quantity
    pass


def apply_discount(total, quantity):
    # Takes the total cost (float) and quantity (int)
    # If quantity is 3 or more, apply a 10% discount
    # Return the final cost either way (float)
    pass


def get_daily_special():
    # Pick a random item from a list of 4 specials
    # Return the name of the special (str) - do not print it
    pass


def main():
    # Print a welcome message
    # Call get_daily_special() and print the result

    # while True loop:
    #   Show the menu using show_menu()
    #   Get the user's choice
    #
    #   if choice == "1":
    #       Ask which drink (1-3)
    #       Call get_drink_price() and store the return value
    #       Print the price here in main()
    #
    #   elif choice == "2":
    #       Ask for price and quantity
    #       Call calculate_total() and store the return value
    #       Print the total here in main()
    #
    #   elif choice == "3":
    #       Ask for price and quantity
    #       Call calculate_total() to get the total
    #       Pass that total into apply_discount() and store the return value
    #       Print the result here in main()
    #
    #   elif choice == "4":
    #       Print a goodbye message
    #       break
    #
    #   else:
    #       Print an invalid input message
    pass


main()