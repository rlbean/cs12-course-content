'''
Name: Bean
Date: June 2, 2026
Assignment: Animal Shelter Demo
Description: A walkthrough of OOP concets using an animal shelter program
'''

# Animal Class - 2 starting variables - name & age (later - intake_date, status)

# ============================================================================
# PARENT CLASS 
# ============================================================================

class Animal:
    '''Represents an animal at the shelter'''
    # The __init__ method runs automatically when we create a new Animal
    # 'self' refers to the specific Animal we are building. 
    def __init__(self, name, age_years, intake_date, status):
        self.name = name
        self.age_years = age_years
        self.intake_date = intake_date
        self.status = status

    # get_info() output
    def get_info(self):
        '''Return a formatted string with this animal's info.'''
        return f"{self.name} (age: {self.age_years}) - {self.status}, intake: {self.intake_date}"
    
    def make_sound(self):
        return f"{self.name} makes a sound"

# =========================================================
# SUBCLASS 1: DOG (CHILD)
# =========================================================
class Dog(Animal):
    '''A dog at the shelter'''

    def __init__(self, name, age_years, intake_date, status, breed, weight_kg, energy_level):
        #super().__init__(...) calls the parent's __init__
        # so we don't have to rewrite the name = name, age = age, etc. 
        super().__init__(name, age_years, intake_date, status)

        #Then we set the dog-specific attributes
        self.breed = breed
        self.weight_kg = weight_kg
        self.energy_level = energy_level
    
    def make_sound(self):
        return f"{self.name} - barks!"
    
    def get_info(self):
        #Override the parent's get_info() with dog specific details. 
        return f"[Dog] {self.name} - {self.breed}, {self.weight_kg} kg, energy: {self.energy_level} (status: {self.status}"


# ===================================================================
# SUBCLASS 2: CAT
# ===================================================================
class Cat(Animal):
    '''A cat at the shelter.'''

    def __init__(self, name, age_years, intake_date, status, coat_pattern, weight_kg, is_indoor_only):
        super().__init__(name, age_years, intake_date, status)
        self.coat_pattern = coat_pattern # 'tabby', 'calico', 'tuxedo', etc.
        self.weight_kg = weight_kg
        self.is_indoor_only = is_indoor_only # True or False
    
    def make_sound(self):
        return f"{self.name} - meows!"
    
    def get_info(self):
        #                  True                                     False
        indoor_text = 'indoor only' if self.is_indoor_only else "indoor/outdoor"
        return f"[Cat] {self.name} - {self.coat_pattern}, {self.weight_kg} kg, {indoor_text} (status: {self.status}"


# ===================================================================
# SUBCLASS 3: BIRD
# ===================================================================
class Bird(Animal):
    '''A bird at the shelter'''

    def __init__(self, name, age_years, intake_date, status, bird_type, wingspan_cm, can_talk):
        super().__init__(name, age_years, intake_date, status)
        self.bird_type = bird_type
        self.wingspan_cm = wingspan_cm
        self.can_talk = can_talk

    def make_sound(self):
        return f"{self.name} chirps loudly!"
    
    def get_info(self):
        #                  True                                     False
        #talker = 'can mimic speech' if self.can_talk else "does not talk"
        
        if self.can_talk == True:
            talker = "can mimic speech"
        else:
            talker = "does not talk"
        
        return f"[Bird] {self.name} - {self.bird_type}, wingspan {self.wingspan_cm} cm, {talker} (status: {self.status}"


#Call Animal class
# animal1 = Animal('Spot', 4,"2025-09-15", 'available')

# #Make one of each
# whiskers = Cat('Mr. Whiskers', 9, '2026-06-02', 'medical hold', 'calico', 4.2, True)
# kiwi = Bird('Kiwi', 2, '2025-10-05', 'available', 'Cockatiel', 32, False)

# #Make a Dog
# rex = Dog('Rex', 3, '2025-08-22', 'available', 'Border Collie', 18.5, 'high')

# animals = [rex, whiskers, kiwi]

# for a in animals:
#     print(a.get_info())



# print(rex.breed) # Dog only attribute
# print(rex.get_info()) # inherited from Animal 
# print(rex.make_sound()) #

# print(whiskers.get_info()) # cat information
# print(kiwi.get_info()) #bird information

#Access their attributes with dot notation
#print(animal1.name)
#print(f"{animal2.name} is {animal2.age_years} year old!")
#print(animal2.get_info())