'''
Name:
Date:
Assignment: #2B - Food Truck Frenzy
Description: An ordering system for Taco Loco food truck. The user selects a taco style and number of toppings, then the program calculates the total cost of their order.
'''

# --------------------------------------------------
# STEP 1 - Display a welcome message to the user
# --------------------------------------------------

# Print a welcome message for "Taco Loco" - or whatever you want to name it.
# Print a short description telling the user what the program does.


# --------------------------------------------------
# STEP 2 - Display the taco menu and get the user's choice
# --------------------------------------------------

# Print the menu of taco styles with their prices:
# 1 - Hard Shell - $3.50
# 2 - Soft Burrito - $4.25
# 3 - Quesidilla - $4.75
# 4 - Taco Salad - $5.00
# 5 - Rice Bowl - $3.75


# Ask the user to enter a number (1-5) to choose their taco style
# Store their answer in a variable called taco_choice (remember: input() gives you a string!)

# Validate taco_choice:
# IF taco choice is 1
# set the name and price
# ELSE IF taco choice is 2
# set the name and price
# ELSE IF choice is 3
# set the name and price
# and so on ... for 4 and 5
# ELSE
# print an error message
# STOP the program or ask again -- your choice

# --------------------------------------------------
# STEP 3 - Get the number of toppings
# --------------------------------------------------

# Tell the user they can choose between 0 and 6 toppings.
# List the available toppings: queso, guac, extra cheese, salsa, chicken, beef

# Ask the user to enter how many toppings they want
# Store their answer in a variable

# Validate number of toppings
# IF toppings is less than 0 or greater than 6
# Print error and stop the program (or ask again -- your choice)

# --------------------------------------------------
# STEP 4 - Calculate the total
# --------------------------------------------------

# Set the TOPPING_COST to 0.75 (this is a constant -- it never changes)

# Calculate toppings subtotal = number of toppings * TOPPING_COST
# Calculate total = base price + topping subtotal

# --------------------------------------------------
# STEP 5 (EXTENSION) - Apply a discount if toppings are more than 4
# --------------------------------------------------

# IF number of toppings is greater than or equal to 4
# Calculate discount amount = toppings subtotal * 0.10
# Subtract the discount from the total
# Make a note that a discount was applied (store a True/False in a variable for example)


# --------------------------------------------------
# STEP 6 - Display the receipt
# --------------------------------------------------

#Print a summary that shows:
# - taco style chosen and its base price
# - number of toppings and their cost
# - EXTENSION - if a discount was applied, show the discount amount
# - final total - formatted to 2 decimal places.

# Example output (no discount):
# --- Your Order ---
# Soft Burrito:     $4.25
# 3 toppings:       $2.25
# -----------------------
# Total:            $6.50

# Example output with discount:
# --- Your Order ---
# Taco Salad         $5.00
# 4 toppings         $3.00
# Discount (10%)    -$0.30
# --------------------------
# Total:             $7.70
