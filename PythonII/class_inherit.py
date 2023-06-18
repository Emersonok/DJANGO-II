# INHERITANCE

class Animal:
    
    def __init__(self) -> None:
        print("Animal created")
        
    def you_now(self):
        print("Animal")
        
    def action(self):
        print("eating")
        
class Dog(Animal):
    
    def __init__(self):
        super().__init__()
        # Animal.__init__(self)
        print("Dog created")
        
    def bark(self):
        print("woof")
        
mydog = Dog()
mydog.you_now()
mydog.action()
mydog.bark()