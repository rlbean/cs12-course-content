'''
Name:
Date:
Assignment: The Café Order Desk - #4
Description:
'''

# =============================================================================
# ASSIGNMENT #5 — MULTIPLE METHODS: CHOOSE YOUR THEME
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# OPTION B -  THE CAFÉ ORDER DESK
# ─────────────────────────────────────────────────────────────────────────────
# A menu-driven café utility with 4 tools + exit.
#
# Menu:
#   1 - Tip Calculator  → calculate_tip(bill, tip_percent)          → tuple
#   2 - Order Total     → total_order(prices)                       → tuple
#   3 - Bill Splitter   → split_bill(total, num_people)             → tuple
#   4 - Discount Checker→ apply_discount(price, discount_percent)   → tuple
#   5 - Exit
#
# Shared primitive: apply_percent(amount, percent) — called by tools 1, 2, 4
# ─────────────────────────────────────────────────────────────────────────────


def apply_percent(amount, percent):
    '''
    Returns the calculated portion of an amount at a given percentage.
    This is a shared utility — called by calculate_tip(), total_order(),
    and apply_discount(). Never called directly by main(). Never prints.

    Parameters: amount (float), percent (float)
    Returns: float

    Example: apply_percent(45.00, 15) → 6.75
    '''
    # TODO: return amount * (percent / 100)
    pass


def calculate_tip(bill, tip_percent):
    '''
    Calculates the tip amount and the total bill.
    Calls apply_percent() to compute the tip.
    Does NOT print — returns both values as a tuple.

    Parameters: bill (float), tip_percent (float)
    Returns: tuple (tip_amount, total)
    '''
    # TODO: call apply_percent(bill, tip_percent) to get the tip amount
    # TODO: calculate the total (bill + tip)
    # TODO: return tip_amount, total
    pass


def total_order(prices):
    '''
    Calculates the subtotal, tax (8%), and grand total for a list of item prices.
    Calls apply_percent() to compute the tax.
    Does NOT print — returns all three values as a tuple.

    Parameters: prices (list of floats)
    Returns: tuple (subtotal, tax, total)
    '''
    # TODO: sum the prices list to get the subtotal
    # TODO: call apply_percent(subtotal, 8) to get the tax
    # TODO: calculate the total (subtotal + tax)
    # TODO: return subtotal, tax, total
    pass


def split_bill(total, num_people):
    '''
    Divides a total bill evenly among a number of people.
    Uses floor division for the per-person amount.
    Uses modulus to find any leftover cents.
    Does NOT print — returns both values as a tuple.

    Parameters: total (float), num_people (int)
    Returns: tuple (per_person, remainder)

    Tip:
        per_person = total // num_people
        remainder  = total %  num_people
    '''
    # TODO: calculate per_person using floor division
    # TODO: calculate remainder using modulus
    # TODO: return per_person, remainder
    pass


def apply_discount(price, discount_percent):
    '''
    Calculates the discount amount and the final price after the discount.
    Calls apply_percent() to compute the savings.
    Does NOT print — returns both values as a tuple.

    Parameters: price (float), discount_percent (float)
    Returns: tuple (savings, final_price)
    '''
    # TODO: call apply_percent(price, discount_percent) to get savings
    # TODO: calculate final_price (price - savings)
    # TODO: return savings, final_price
    pass


def show_menu():
    '''
    Displays the Café Order Desk menu and returns the user's validated choice.
    Keeps asking until a valid integer between 1 and 5 is entered.

    Returns: int (1–5)
    '''
    print()
    print("------------------------------------")
    print("---- The Café Order Desk ----")
    print("------------------------------------")
    print("    - 1 -  Tip Calculator")
    print("    - 2 -  Order Total")
    print("    - 3 -  Bill Splitter")
    print("    - 4 -  Discount Checker")
    print("    - 5 -  Exit")
    print("------------------------------------")

    # TODO: get and validate the user's choice (must be 1–5)
    # TODO: return the validated integer choice
    pass


def exit_program():
    '''Prints a farewell message. Called by main() before break.'''
    print("Thanks for visiting the Café Order Desk. Come back soon!")


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
            # TODO: print the tip and total, formatted with $ and 2 decimal places
            pass

        elif choice == 2:
            # Order Total
            # TODO: ask how many items are in the order
            # TODO: loop to collect each item price into a list
            # TODO: call total_order(prices)
            # TODO: print the subtotal, tax, and total — all formatted with $
            pass

        elif choice == 3:
            # Bill Splitter
            # TODO: get the total amount and number of people from the user
            # TODO: call split_bill(total, num_people)
            # TODO: print the per-person amount and any remainder
            pass

        elif choice == 4:
            # Discount Checker
            # TODO: get the original price and discount percentage from the user
            # TODO: call apply_discount(price, discount_percent)
            # TODO: print the savings and the final price, formatted with $
            pass

        elif choice == 5:
            exit_program()
            break

        # --- EXTENSION ---
        # Add an elif choice == 6 block for your custom tool.
        # Your tool must accept at least 1 parameter, return a value,
        # and call apply_percent() (or another existing function) inside it.


main()