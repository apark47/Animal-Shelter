# Animal.py

class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        self.weight = weight
        self.age = age
        if species == None:
            self.species = species
        else:
            self.species = species.upper()

        if name == None:
            self.name = name
        else:   
            self.name = name.upper()
        
    def setSpecies(self, species):
        self.species = species.upper()
        
    def setWeight(self, weight):
        self.weight = weight
        
    def setAge(self, age):
        self.age = age
        
    def setName(self, name):
        self.name = name.upper()
        
    def toString(self):
        result = "Species: " + str(self.species.upper()) + \
                 ", Name: " + str(self.name.upper()) + ", Age: " + str(self.age) + ", Weight: " + str(self.weight)
        return result

#a = Animal("dog", 12.2, 2)
#print(a.toString())
