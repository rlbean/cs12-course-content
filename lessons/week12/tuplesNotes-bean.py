points = (3, 4)
print(points[0])
colours = ("red", "green", "blue","yellow")
print(colours[1])
print(colours[-2])

# points[0] = 5 # can't do this

subset = colours[1:4]
print(colours[:2])
print(colours[2:])
print(subset)

length = len(colours)

print(length)

repeatIt = colours *2

print(colours *2)
moreColours = ("purple", "cyan")
combinedColours = colours + moreColours
print(combinedColours)

var1, var, var3, var4, var5, var6 = combinedColours
print(var1)
print(var5)

var1 = "Hello"
print(var1)
var1, var, var3, var4, var5, var6 = combinedColours
print(var1)
print(var5)

votes = ('Yes', 'No', "No", "Yes", "No", "No")
print(votes.count("Yes"))
