class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    
    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

r1 = Rectangle(4, 5)
r2 = Rectangle()

print("Dimensions of r1:")
r1.display()
print("Dimensions of r2:")
r2.display()

print("Width of r1 and r2:")
print(f"{r1.width} & {r2.width}")
print("Height of r1 and r2:")
print(f"{r1.height} & {r2.height}")