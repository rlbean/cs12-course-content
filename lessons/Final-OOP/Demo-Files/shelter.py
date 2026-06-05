'''
Name Bean - Animal Shelter Demo
Date: June 2026
Assignment: Animal Shelter Demo - 
Description: The Shelter class that manages a collection of animals. 
'''

from animal_demo import Animal, Dog, Cat, Bird

# ========================================================================
# SHELTER CLASS - Manages the collection of animals
# ========================================================================

class Shelter:
    '''Manages a collection of animals at the shelter.'''

    def __init__(self, name):
        self.name = name
        self.animals = [] # list to hold the animals - dog, cat, bird, rabbit

    def add_animal(self, animal):
        '''Add a new animal to the shelter.'''
        self.animals.append(animal) # add the animal to the list - one at a time

    def get_all_animals(self):
        '''Return the full list of animals. '''
        return self.animals
    
    def get_count(self):
        '''Return how many animals are at the shelter.'''
        return len(self.animals)
    

