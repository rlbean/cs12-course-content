'''
Name: Bean - Animal Shelter Demo
Date: June 2026
Assignment: Final - Shelter Demo
Description: The main program. Runs the menu loop and handles user input/output. 
'''

from shelter import Shelter
from animal_demo import Animal, Dog, Cat, Bird

def print_menu():
    print("\n===== Animal Shelt Manager =====")
    print("1. Add an animal")
    print("2. View all animals.")
    print("3. Hear them speak")
    print("4. Quit")

def main():
    # create the shelter
    shelter = Shelter('Sunnyside Rescue')
    #load from the file -- later situation

    #while loop - for printing menu
    while True:
        #display options to user
        print_menu()
        #get input from user
        choice = input("Choose an option by entering the number: ").strip()

        #what did the user choose -- if option 1
        if choice == "1":
            print("Add animal")
        elif choice == "2":
            print("view all animals")
        elif choice == "3":
            print("hear them speak")
        elif choice == "4":
            print("quit the program")
            break
        else:
            print("You didn't choose a valid option. Please enter 1, 2, 3, or 4")

main()

# #Make one of each
# whiskers = Cat('Mr. Whiskers', 9, '2026-06-02', 'medical hold', 'calico', 4.2, True)
# kiwi = Bird('Kiwi', 2, '2025-10-05', 'available', 'Cockatiel', 32, False)
# rex = Dog('Rex', 3, '2025-08-22', 'available', 'Border Collie', 18.5, 'high')

# #Test Shelter
# shelter = Shelter('Sunnyside Rescue')
# shelter.add_animal(rex)
# shelter.add_animal(whiskers)
# shelter.add_animal(kiwi)

# for a in shelter.get_all_animals():
#     print(a.get_info())