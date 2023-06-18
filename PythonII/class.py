class Dog:
    
    #CLASS OBJECT ATTRIBUTES
    species = "mammal"
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog("Jutsi", "Dolly")
new_dog = Dog("German Sheperd", "Green")
print(mydog.breed)
print(new_dog.name)
print(mydog.species)