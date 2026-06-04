'''
Name
Date
Assignment
Description
'''

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
    

