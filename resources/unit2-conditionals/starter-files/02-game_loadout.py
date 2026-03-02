'''
Name:
Date:
Assignment: #2C - Game Loadout Builder
Description: A hero builder tool for an RPG. The player selects a character class and equips power-ups. The program calculates their total power score before heading into battle.
'''

# --------------------------------------------------
# STEP 1 - Display a welcome message to the user
# --------------------------------------------------

# Print a dramatic welcome message for the "Hero Builder" tool
# Tell the player they need to choose their class and equip power-ups


# --------------------------------------------------
# STEP 2 - Display the class menu and get the player's choice
# --------------------------------------------------

# Print the class selection menu:
# 1 - Warrior   Base Power: 120     +15 per power-up
# 2 - Mage      Base Power: 100     +20 per power-up
# 3 - Rogue     Base Power: 110     +18 per power-up
# 4 - Paladin   Base Power: 130     +12 per power-up

# Ask the player to end a number (1-4) to select their class
# Store their answer in a variable - remember that input() is a string!

# Validate class choice
# IF class choice --> 1
# set name, base power, and powerup bonus
# IF class choice --> 2
# set name, base power, and powerup bonus
# and so on for 3 and 4
# ELSE
# Print an error message and stop


# --------------------------------------------------
# STEP 3 - Get the number of power-ups
# --------------------------------------------------

# Tell the player they can equip between 1 and 5 power-ups
# Ask the player to enter how many power-ups they want
# Store it in a variable -- making sure to convert to the right data type!

# Validate number of powerups
# IF number of powerups is less than 1 or greater than 5
# Print an error and stop the program


# --------------------------------------------------
# STEP 4 - Calculate total power score
# --------------------------------------------------

# Calculate powerup total = number of powerups * powerup bonus
# Calculat total power = base power + powerup total


# --------------------------------------------------
# STEP 5 (EXTENSION) - Check for Legendary Bonus
# --------------------------------------------------

# IF number of powerups is 5
# set legendary bonus, add bonus to total power
# Store that the bonus was earned -- maybe in a true/false variable?


# --------------------------------------------------
# STEP 6 - Display the loadout summary
# --------------------------------------------------

# Print a summary that shows:
# - class chosen and their base power
# - number of power-ups equipped and total bonus earned
# - EXTENSION - if legendary bonus was earned, show it separately
# - the final total power score

# Example output (no legendary bonus):
# --- Hero Loadout ---
# Class:            Rogue
# Base Power:       110
# 3 Power-Ups:      +54
# ---------------------
# Total Power:      164
# Battle Rating:    Ready for combat!

# Example output - with legendary bonus:
# --- Hero Loadout ---
# Class:            Mage
# Base Power:       100
# 5 Power-Ups:      +100
# LEGENDARY BONUS:  +50
# -----------------------
# Total Power:      250
# Battle Rating:    LEGENDARY WARRIOR!


# Hint - You could use if/elif/else on the total power score to show different "battle rating" messages