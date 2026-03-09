'''
Name:
Date:
Assignment: #2E - Movie Night Booking
Description: A ticket kiosk app for StarPlex Cinemas. The customer selects a seat type and orders snacks. The program calculates the total cost of their movie night.
'''


# --------------------------------------------------
# STEP 1 - Display a welcome message to the user
# --------------------------------------------------

# Print a welcome message for "StarPlex Cinemas"
# Tell the customer you'll help them book their perfect movie night


# --------------------------------------------------
# STEP 2 - Display the seat types and get the customer's choice
# --------------------------------------------------

# Print the seating menu:
# 1 - Regular       $10.00 (standard seating)
# 2 - Premium       $13.00 (recliner sears, extra legroom)
# 3 - VIP           $17.00 (private section, waitstaff)
# 4 - IMAX          $15.00 (giant screen, enhanced sound)


# Ask the customer to enter a number (1-4) to select their seat type
# Store their answer in a variable for the seat choice - remember that the input() is a string

# Validate seat choice
# IF seat choice is 1
# set the name and price
# ELSE IF the seat choice is 2
# set the name and price
# and so on for 3 & 4
# ELSE
# Print a error message and stop the program -- or ask again


# --------------------------------------------------
# STEP 3 - Get the number of snacks
# --------------------------------------------------

# Tell the customer they can order between 0 and 5 snacks
# popcorn, nachos, candy, hot dog, drink, pretzel - for example


# Ask the customer to enter how many snacks they want (0 is allowed)
# Store it in the variable -- convert to the proper data type


# Validate number of snacks
# IF number of snacks is less than 0 or greater than 5
# Print an error, stop the program


# --------------------------------------------------
# STEP 4 - Calculate the total
# --------------------------------------------------

# Set the SNACK_COST to $4.50 (each snack costs $4.50) - it is a constant


# Calculate snack subtotal = number of snacks * SNACK_COST
# Calculate total = ticket price + snack subtotal


# --------------------------------------------------
# STEP 5 EXTENSION - Apply the Snack Pack Deal if snacks  is 3 or more
# --------------------------------------------------

# IF numbe rof snacks is great than or equal to 3
# Set SNACK_DEAL_DISCOUNT to 3.00
# Subtract the discount from the total
# Store that the deal was applied (true/false) variable


# --------------------------------------------------
# STEP 6 - Display the receipt
# --------------------------------------------------

# Print a summary that shows:
# - seat type chosen and its ticket price
# - the number of snacks and their subtotal
# - EXTENSION - If the Snack Pack Deal was applied -- show the $3.00 savings
# - the final total - formatted to 2 decimal places.

# Example  output - no deal:
# --- Your Booking ---
# Premium Seat:     $13.00
# 2 Snacks:         $9.00
# -----------------------------
# Total:            $22.00


# Example output - with Snack Pack Deal:
# --- Your Booking ---
# VIP Seat:          $17.00
# 4 Snacks:          $18.00
# Snack Pack Deal:  -$3.00
# --------------------------
# Total:             $32.00

# Note: What should your output look like if the customer orders 0 snacks?
# 0 Snacks: $0.00 is valid --> make sure it still displays correctly.