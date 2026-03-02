'''
Name:
Date:
Assignment: #2D - Flex Fitness Day Pass
Description: A kiosk app for Flex Fitness gym. The visitor selects a day pass tier and any add-ons they would like. The program calculates total cost of their visit.
'''


# --------------------------------------------------
# STEP 1 - Display a welcome message to the user
# --------------------------------------------------

# Print a welcome message for "Flex Fitness" -- or whatever you want to call it
# Tell the visitor you'll help them set up their day pass


# --------------------------------------------------
# STEP 2 - Display the pass tiers and get the visitor's choice
# --------------------------------------------------

# Print the day pass menu:
# 1 - Basic         $10.00 (gym floor access only)
# 2 - Standard      $15.00 (gym + group classes)
# 3 - Premium       $20.00 (gym + classes + pool)
# 4 - Elite         $28.00 (full access, no restrictions)


# Ask the visitor to enter a number (1-4) to select their pass
# Store the answer in a variable -- remember it is a string!


# Validate pass choice
# IF pass choice is 1
# set name, tier price
# so on....2, 3, and 4
# ELSE
# print an error message and stop (or re-ask)


# --------------------------------------------------
# STEP 4 - Calculate the total
# --------------------------------------------------

# Set ADDON_COST to $6.00 -- each add-on is $6.00 -- this is a constant


# Calculate addons subtotal = number of addons * ADDON_COST
# Calculate total = tier price + addons subtotal


# --------------------------------------------------
# STEP 5 (EXTENSION) - Apply a discount if add-ons greater than or equal to 2
# --------------------------------------------------

# IF number of addons is great than or equal to 2
# Calculate discount amount = addons subtotal * 0.15
# Subtract discount amount from total
# Store that a discount was applied (true/false variable for example)



# --------------------------------------------------
# STEP 6 - Display the receipt
# --------------------------------------------------

# Print a summary that shows
# - The pass tier chosen and its price
# - the number of add-ons and their subtotal
# - EXTENSION - if a discount was applied, show the discount amount
# - the final total - formatted to 2 decimal places


# Example output - no discount:
# --- Your Day Pass ---
# Standard Pass:        $15.00
# 1 Add-On:             $6.00
# -----------------------------
# Total:                $21.00


# Example output with discount:
# --- Your Day Pass ---
# Preium Pass:           $20.00
# 3 Add-Ons:             $18.00
# Discount (15%):       -$2.70
# -------------------------------
# Total:                 $35.30

# Note: What should happen if number of addons is 0?
# Make sure your output still makes sense.