'''
Name:        
Date:        
Assignment:  Colour Spinner - Teaching Demo
Description: 
'''

import random


# --------------------------------------------------
# spin_wheel()
# Picks a random section (1-4) and returns a colour.
# --------------------------------------------------

def spin_wheel():
    # TODO: Generate a random number between 1 and 4
    random_number = random.randint(1,4)
    print("randum_number - ", random_number)
    # TODO: Return "Red" for 1, "Blue" for 2, "Green" for 3, "Yellow" for 4
    if random_number == 1:
        #print("Red")
        return "Red"
    elif random_number == 2:
        #print("Blue")
        return "Blue"
    elif random_number == 3:
        #print("Green")
        return "Green"
    elif random_number == 4:
        #print("Yellow")
        return "Yellow"
    else:
        #print("You picked a wrong number")
        return "Error"
    #pass # will add code later - prevents errors when Python expects a statement
    #... # we can use 3 periods or an ellipsis as well


#colour_choice = spin_wheel()
#print(colour_choice)

# --------------------------------------------------
# get_points(colour)
# Receives a colour string. Returns the point value.
#   Red    -> 50 pts
#   Blue   -> 30 pts
#   Green  -> 20 pts
#   Yellow -> 10 pts
# --------------------------------------------------
def get_points(colour):
    # TODO: Use if/elif/else to return the right point value
    if(colour == "Red"):
        return 50
    elif (colour == "Blue"):
        return 30
    elif (colour == "Green"):
        return 20
    else: 
        return 10
    # Hint: put the rarest/highest outcome first
    print(colour)
    pass

#pts = get_points(colour_choice)
# --------------------------------------------------
# get_num_spins()
# Asks the user how many spins they want (1-8).
# Validates the input. Returns a valid integer.
# --------------------------------------------------
def get_num_spins():
    while True:
        user_input = input("How many spins would you like? (1-8): ")

        # TODO: Check that user_input is a digit
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= 8:
                return num
        print("Please enter a whole number between 1 and 8")
        # TODO: Convert to int and check it is between 1 and 8
        # TODO: If valid, return it
        # TODO: If invalid, print a helpful error message

        pass

#spins = get_num_spins()
# --------------------------------------------------
# play_game(num_spins)
# Runs the spin loop for the given number of rounds.
# Accumulates and returns the total score.
# --------------------------------------------------
def play_game(num_spins):
    total_score = 0

    # TODO: Use a for loop to repeat num_spins times
    for i in range(1, num_spins+1):
        print(i)
        # TODO: Call spin_wheel() and store the colour
        colour_choice = spin_wheel()
        # TODO: Call get_points() with that colour and store the points
        pts = get_points(colour_choice)
        # TODO: Add points to total_score
        total_score = total_score + pts
        # TODO: Print each round: spin number, colour, and points
        print(f"  Spin {i}: {colour_choice} -- > {pts} pts")

    return total_score      # sends the total back to main() — don't remove this

#print(play_game(spins))
# --------------------------------------------------
# main()
# Controls the overall flow. All final output lives here.
# --------------------------------------------------
def main():
    print("================================")
    print("        COLOUR SPINNER          ")
    print("================================\n")

    # TODO: Call get_num_spins() and store the result
    spins = get_num_spins()
    # TODO: Call play_game() with that number and store the score
    score = play_game(spins)
    # TODO: Print the final score
    print(f"\n----- Final Score: {score} -----")
    # TODO: Print a final message based on the score:
    #         150+  -> "Amazing run - you're on fire!"
    #         80-149 -> "Pretty good spin!"
    #         below 80 -> "Better luck next time."
    if score >= 150:
        print("Amazing run - you're on fire!")
    elif score >= 80:
        print("Pretty good spin!")
    else:
        print("Better luck next time.")


main()