# Week 4 --> Feb. 23rd - 26th

#cup_size = 12
base_cost = 2.00
name = "Bean"

print("Welcome to Tec-Voc Coffee!")
print()
print("Available Sizes:")
print("  Small  -  8 oz")
print("  Medium - 12 oz")
print("  Large  - 16 oz")
print("  XLarge - 20 oz")

cup_size = int(input("What size drink would you like? "))

#conditional statement using or
# if (cup_size == 8 or cup_size == 12 or cup_size == 16 or cup_size == 20):
#     print("Valid Choice")
# else:
#     print("Invalid Choice")

if cup_size in [8,12,16,20]:
    print("Valid")
else:
    print("Invalid")





#number of add-ins
addins_number = int(input("How many extra add-ins do you want? "))
#addins_number = input("How many extras? ")

# if addins_number == 2:
#     print("You chose 2 extras -- oat milk and vanilla!")
# elif addins_number == 3:
#     print("You chose 3 extras!")
# else:
#     print("Invalid choice - sorry we can only do 1-5 extras!")

#range
# if 0 <= addins_number <= 5:
#     print("Great you picked the right amount!")
# else:
#     print("Invalid selection")





print(type(addins_number))

addin_cost = 0.25 * addins_number * cup_size

print(f"Total extra cost is -- {addin_cost:.2f}")
