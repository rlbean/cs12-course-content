'''
Name: Teacher Solution
Date: 2026
Assignment: Assignment 4 Demo – Cafe Order Desk
Description: A menu-driven cafe ordering program that demonstrates
             multiple functions with return values and a while True loop.
             TEACHER COPY - do not distribute to students.
'''

import random

# ─────────────────────────────────────────────────────────────
# RULE: Helper functions use RETURN, not print.
#       main() is the ONLY function that prints output.
# ─────────────────────────────────────────────────────────────


def show_menu():
    '''
    Builds the main menu as a formatted string.
    Returns: str - the full menu prompt (no newline at end so input() follows inline)
    '''
    menu = (
        "\n=== Cafe Order Desk ==="
        "\n1. Check drink price"
        "\n2. Calculate order total"
        "\n3. Check for a discount"
        "\n4. Exit"
        "\nYour choice: "
    )
    return menu  # Return - never print inside a helper function


def get_drink_price(choice):
    '''
    Looks up the price for a drink based on the user's menu choice.
    Parameters: choice (int) - 1, 2, or 3
    Returns: float - the price of the chosen drink, or 0.0 if invalid
    '''
    if choice == 1:
        return 3.50    # Espresso
    elif choice == 2:
        return 4.75    # Latte
    elif choice == 3:
        return 5.25    # Specialty drink
    else:
        return 0.0     # Fallback - always return something


def calculate_total(price, quantity):
    '''
    Calculates the cost of an order.
    Parameters: price (float), quantity (int)
    Returns: float - price multiplied by quantity
    '''
    total = price * quantity
    return total  # Return the result - do not print here


def apply_discount(total, quantity):
    '''
    Applies a 10% discount when the customer orders 3 or more drinks.
    Parameters: total (float), quantity (int)
    Returns: float - the final price after discount (or unchanged if no discount applies)
    '''
    if quantity >= 3:
        return total * 0.90    # 10% off for orders of 3+
    else:
        return total           # No discount - still must return something


def get_daily_special():
    '''
    Randomly selects today's featured drink from a list.
    Returns: str - the name of the daily special
    '''
    specials = ["Caramel Macchiato", "Iced Matcha", "Honey Oat Latte", "Cold Brew Float"]
    index = random.randint(0, len(specials) - 1)
    return specials[index]  # Return the name - main() will print it


def main():
    '''
    Entry point. Runs the while True menu loop.
    This is the ONLY function that calls print().
    '''
    # Welcome message
    print("Welcome to the Cafe Order Desk!")
    print(f"Today's special: {get_daily_special()}")  # Call function, print the return value

    while True:
        # show_menu() returns a string - pass it directly to input()
        choice = input(show_menu())

        if choice == "1":
            # Option 1: Check a drink price
            print("\nDrinks available:")
            print("  1 - Espresso   $3.50")
            print("  2 - Latte      $4.75")
            print("  3 - Specialty  $5.25")
            drink = int(input("Pick a drink (1-3): "))
            price = get_drink_price(drink)   # Store the returned value
            if price > 0:
                print(f"Price: ${price:.2f}")
            else:
                print("Invalid drink choice.")

        elif choice == "2":
            # Option 2: Calculate order total
            price = float(input("\nEnter the drink price: $"))
            qty   = int(input("How many drinks? "))
            total = calculate_total(price, qty)   # Store the returned value
            print(f"Order total: ${total:.2f}")   # main() prints the result

        elif choice == "3":
            # Option 3: Check for a discount
            # Demonstrates chaining - one return value feeds into the next function
            price = float(input("\nEnter drink price: $"))
            qty   = int(input("How many drinks? "))
            total = calculate_total(price, qty)   # Step 1: get total
            final = apply_discount(total, qty)    # Step 2: pass total into discount check
            if qty >= 3:
                print(f"Discount applied! ${total:.2f} → ${final:.2f} (10% off)")
            else:
                print(f"No discount yet (need 3+). Total: ${final:.2f}")

        elif choice == "4":
            # Option 4: Exit - print goodbye then break out of the loop
            print("\nThanks for visiting the Cafe! See you next time.")
            break   # Exits the while True loop - do NOT use exit()

        else:
            # Any other input
            print("Invalid choice. Please enter a number between 1 and 4.")


main()