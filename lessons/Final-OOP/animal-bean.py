#The 4 Pilas of OOP

from abc import ABC, abstractmethod

class Animal(ABC): #this is an abstract class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()