'''
Name:
Date:
Assignment: #4 - The Helper Hub
Description:
'''

import random


# Displays the menu and returns the user's validated choice (1–5)
def show_menu():
    pass


# Calculates the tip amount and total — returns both values back to main()
def calculate_tip():
    pass


# Rolls a single die with a given number of sides — returns the result
def roll_die():
    pass


# Rolls multiple dice by calling roll_die() — returns a list of results
def roll_dice():
    pass


# Converts a temperature between Celsius and Fahrenheit — returns the converted value
def convert_temp():
    pass


# Flips a coin multiple times using roll_die() — returns the heads and tails counts
def flip_coin():
    pass


# Prints a farewell message
def exit_program():
    pass


def main():
    print("Welcome to the Helper Hub!")

    while True:
        choice = show_menu()        # show_menu returns the user's choice

        if choice == 1:
            # Get bill and tip % from the user
            # Call calculate_tip() and receive the result
            # Print tip amount and total
            pass

        elif choice == 2:
            # Ask how many dice and how many sides
            # Call roll_dice() and receive the list of results
            # Print the rolls and their sum
            pass

        elif choice == 3:
            # Ask for a temperature and direction (C or F)
            # Call convert_temp() and receive the result
            # Print the converted temperature
            pass

        elif choice == 4:
            # Ask how many times to flip
            # Call flip_coin() and receive the result
            # Print the heads and tails counts
            pass

        elif choice == 5:
            exit_program()
            break                   # exits the while True loop


main()