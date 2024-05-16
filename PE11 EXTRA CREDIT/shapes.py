from math import pi

class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    
    def display(self):
        print(f"Radius: {self.radius}")
    
    def setRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
    def area(self):
        return pi * self.radius ** 2
    
    def circumference(self):
        return 2 * pi * self.radius
    
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    
    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height
    
    def getWidth(self):
        print(f"Get Width: {self.width}")
    
    def getHeight(self):
        print(f"Get Height: {self.height}")
    
    def area(self):
        return self.width * self.height