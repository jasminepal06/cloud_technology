from rectangle import Rectangle

r1 = Rectangle(4, 5)
r2 = Rectangle()

r1.display()
print(f"Area: {r1.area()}")

r2.display()
print(f"Area: {r2.area()}")

r2.setHeight(6)
r2.setWidth(6)

r2.getHeight()
r2.getWidth()
print(f"Area: {r2.area()}")