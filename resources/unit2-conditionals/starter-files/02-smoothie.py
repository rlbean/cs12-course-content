'''
Name:
Date:
Assignment: #2A - Super Smoothies
Description: A smoothie cost estimator for a local restaurant. The user selects a cup size and number of ingredients. The program calculates the total cost of making their smoothie.
'''


# --------------------------------------------------
# STEP 1 - Dsiplay a welcome message to the user
# --------------------------------------------------

# Print a welcome message for "Super Smoothie" - or whatever you want to call it
# Tell the customer that you need 2 pieces of information to calculate the cost of their smoothie
# Cup size and number of ingredients


# --------------------------------------------------
# STEP 2 - Display the smoothie sizes
# --------------------------------------------------

# Print the available cup sizes:
#   Small       10 oz
#   Medium      12 oz
#   Large       15 oz
#   XLarge      20 oz

# Ask the user to enter the size of their smoothie in oz
# Store their answer in a varialbe and convert it to the correct data type.


# Validate the size size choice
# IF cup size is 10
# Valid choice -- let it through
# ELSE IF -- other choices here too
# ELSE
# Print an error message and stop program - or re-ask



# --------------------------------------------------
# Step 3 - Get the number of ingredients
# --------------------------------------------------

# Tell the user they can choose between 1 and 10 ingredients

# Ask the suer to enter how many ingredients they want
# Store their answer in a variable -- convert it to the correct data type

# Validate the number of ingredients choosen
# IF number of ingredients are less than 1 or greater than 10
# Print an error message and stop the program -- or re-ask

# --------------------------------------------------
# STEP 4 - Calculate the total cost
# --------------------------------------------------

# Set RENT_LABOUR to 1.75 (fixed cost per smoothie, never changes)
# Set INGREDIENT_RATE to 0.10 (cost rate per ingredient per oz)

# Calculate ingredient cost = ingredient rate * number of ingredients * cup size
# Calculate total = rent labour + ingredient cost


# --------------------------------------------------
# STEP 5 (EXTENSION) - apply the Loyalty Card Discount
# --------------------------------------------------

# IF number of ingredients is greater than or equal to 8
# Calculate a discount amount = ingredient cost * 0.10
# subtract discount amount from the total
# Store that a discount was applied - true/false for example



# --------------------------------------------------
# STEP 6 - Display the receipt
# --------------------------------------------------

# Print a summary that shows:
# - The cup size chosen (in oz)
# - the number of ingredients
# - EXTENSION - if a discount was applied, show the discount amount
# - Final cost of the smoothie, formatted to 2 decimal places

# Example output - no discount:
# --- Your Smoothie Cost ---
#   Cup Size:          12 oz
#   Ingredients:        3
# -----------------------------
#   Total Cost:         $5.35


# Example output with discount:
# --- Your Smoothie Cost ---
#   Cup Size:            20 oz
#   Ingredients:         8
#   Discount  (10%)     -$1.60
# ----------------------------
#   Total Cost:         $14.40

