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