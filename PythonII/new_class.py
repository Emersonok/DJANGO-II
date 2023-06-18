class Circle:
    
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def set_radius(self, new_radius):
        self.radius = new_radius
        
mycircle = Circle(3)
mycircle.set_radius(999)
print(mycircle.area())