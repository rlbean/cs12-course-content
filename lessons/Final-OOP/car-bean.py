class Car:
    '''My Car object. Parameters - colour, doors'''
    def __init__(self, name, hp = 0, colour = "Red"):
        self._name = name
        self._hp = hp
        self._colour = colour
    
    def info(self):
        print(f"My {self._colour} {self._name} has {self._hp} hp under the hood")

    def drive(self):
        print(f"{self._name} is driving")

    def stop(self):
        print(f"{self._name} has stopped")
    
    def get_hp(self):
        return self._hp
    
    def set_hp(self, new_hp):
        if new_hp >= 0:
            self._hp = new_hp
        else:
            print("Horsepower must be positive")




my_chevy = Car("Camaro") #give a name and use defaults for other variables
my_ford = Car("Mustang", 480, "Black")

my_chevy.info()
my_ford.info()
print(my_chevy.get_hp())
my_chevy.set_hp(200)
my_chevy.info()