# AnimalShelter.py

from Animal import Animal

class AnimalShelter:

    def __init__(self):
        self.animalshelter = {}


    def addAnimal(self, animal):
        '''Adds an Animal object (animal) to the AnimalShelter.
           The inserted Animal object should be added to the end
           of the list of existing animals that are the same species.
           You may assume that an animal with the same attributes does
           not already exist in the AnimalShelter when this method is called.
        '''
        if self.animalshelter.get(animal.species) == None:
            self.animalshelter[animal.species] = [animal]
        else:
            self.animalshelter[animal.species].append(animal)
       
                        
    def removeAnimal(self, animal):
        '''Removes an Animal object (animal) from the AnimalShelter if it exists.
           Your code will need to check and see if the parameter animal object has
           the same species, name, age, and weight as an existing animal in the
           AnimalShelter if it is to be removed from the AnimalShelter.
        '''
        '''
        if self.animalshelter.get(animal.species) == None:
            return
        else:
            for i in self.animalshelter.get(animal.species):    
                
                if self.animalshelter[animal.species][i].species == animal.species and \
                   self.animalshelter[animal.weight][i].weight == animal.weight and \
                   self.animalshelter[animal.name][i].name == animal.name and \
                   self.animalshelter[animal.age][i].age == animal.age:
                   self.animalshelter[animal.species].pop(i)
                
                if i.species == animal.species and \
                   i.weight == animal.weight and \
                   i.name == animal.name and \
                   i.age == animal.age:
                    self.animalshelter.get(animal.species).remove(i)
        '''
        if animal.species in self.animalshelter:
            self.animalshelter.pop(animal.species)
            
    def removeSpecies(self, species):
        '''Removes all animals of a certain species from the AnimalShelter if it exists.
           Your code will need to remove the species entry from the AnimalShelter’s dictionary.
           Note: the species parameter value may be in either lower / upper case.
        '''
        species = species.upper()
        
        if species in self.animalshelter.keys():
            del self.animalshelter[species]
             
    def getAnimalsBySpecies(self, species):
        '''Returns a string of all animals of a certain species. This string should consist
           of a collection of strings - one line for each animal. Since each animal will be
           in its own line within a single string, a newline character (\n) should be inserted
           between each line (if applicable) EXCEPT at the very last line where no newline
           character should exist). The order of the Animals in this string will be dictated
           by the order of the Animals in the AnimalShelter’s list for the Animal’s species.
           The Animal toString() method should be used when constructing this method’s return
           string. If no Animals of the species exist in the AnimalShelter, then this method
           returns an empty string (""). Note: the species parameter value may be in either lower / upper case.
        '''
        species = species.upper()
        
        if species not in self.animalshelter:
            return ""

        if self.animalshelter.get(species) != None:
            species_animals = ""
        
            for index, element in enumerate(self.animalshelter.get(species)):
                if element == self.animalshelter.get(species)[-1]:
                    species_animals += (element.toString())
                else:
                    species_animals += (element.toString() + "\n")

        return species_animals
        
    def doesAnimalExist(self, animal):
        '''Returns True if the parameter animal (with matching species, name, age, and weight)
           exists in the AnimalShelter. Returns False otherwise.
        '''

        if self.animalshelter.get(animal.species) == None:
            return False
        else:

            for i in self.animalshelter.get(animal.species):    
                
                if i.species == animal.species and \
                   i.weight == animal.weight and \
                   i.name == animal.name and \
                   i.age == animal.age:
                    return True

                else:
                    return False

                '''
                if self.animalshelter[animal.species][i].species == animal.species and \
                   self.animalshelter[animal.weight][i].weight == animal.weight and \
                   self.animalshelter[animal.name][i].name == animal.name and \
                   self.animalshelter[animal.age][i].age == animal.age:
                   self.animalshelter[animal.species].pop(i)
                '''

