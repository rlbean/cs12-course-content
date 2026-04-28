#          0,1,2,3,4,5,
numbers = [1,2,3,4,5,6, "HELLO", "Goodbye"]
print(len(numbers))

print(f"numers - {numbers[6]}")


print(f"Slice - {numbers[1:4]}")
#              0         1           2            3           4
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# print(f"Slice at - {weekdays[:3]}")

# weekdays[0] = "WHOMP-WHOMP"

print(weekdays)

# weekdays.append("Saturday")
# print(weekdays)
# print(weekdays)
# weekdays.remove("Wednesday")
# print(weekdays)

weekdays.pop(1)
print(weekdays)

#           0           1          2
fruits = ["apples", "oranges", "pears"]
print(fruits)

fruits.insert(1, "watermelon")
print(fruits)
print()

students = [['John', '15', 'Computer Science'], ['Jane', '14','Socials']]
print(students[1][2])
