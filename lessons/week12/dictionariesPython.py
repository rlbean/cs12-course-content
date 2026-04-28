studentA = {"name": "Alice", 'age': 16, 'grade': 'A'}
print(studentA)
print(studentA['grade'])
print(f"{studentA['name']} earned a {studentA['grade']}, on the test on her {studentA['age']}th birthday!")

studentF = {'name': 'Bean', 'age': 'nevermind', 'grade': 'F'}
print(studentF)

studentF['grade'] = 'D'
studentF['city'] = "Winnipeg"
print(studentF)

del studentF['grade']
print(studentF)
print(studentF.keys())
print(studentF.values())
print(studentF.items())

name = studentF.get('grade')
print(name)

studentB = {'name':{'first': 'Bobbi', 'last': 'Bean'}, 'age': 'old'}
print(studentB['name']['first'])