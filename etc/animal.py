class Animal:
    def __init__(self, name, gender, age, species):
        self.name = name  # Public attribute 
        if gender:
            if 'F' in gender.upper():
                self.gender = 'Female'
            else:
                self.gender = 'Male'
        else:
            print("Gender must be 'M' or 'F'")
            
        self._age = age   # Semi-private
        self.__species = species  # Private (name-mangled)

    def describe(self):
        print(f"This is {self.name}, a {self.gender.lower()} {self.__species} who is {self._age} years old.")

    def get_age(self):
        return self._age

    def get_species(self):
        return self.__species

    def set_age(self, new_age):
        if new_age > self._age:
            self._age = new_age
        else:
            print("Age must be positive and greater than current age!")

    def make_sound(self):
        print("Generic animal sound.")

class Bird(Animal):
    def __init__(self, name, gender, age, species, wingspan):
        super().__init__(name, gender, age, species)
        self.wingspan = wingspan

    def make_sound(self):
        print("Chirp!")

class Mammal(Animal):
    def __init__(self, name, gender, age, species, fur_color):
        super().__init__(name, gender, age, species)
        self.fur_color = fur_color

    def make_sound(self):
        print("Roar!")

# Main code
zoo_animals = [
    Animal("Generic", "female", 5, "Unknown"),
    Bird("Eagle", "femle", 7, "Bird", 2.5),
    Mammal("Lion", "male", 4, "Mammal", "Golden")
]
for animal in zoo_animals:
    animal.make_sound()  # Different outputs!
