from shapes import Rectangle, Circle

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

c1 = Circle()
c2 = Circle(10)

c1.display()
print(f"Area: {c1.area()}")
print(f"Circumference: {c1.circumference()}")

c2.display()
print(f"Area: {c2.area()}")
print(f"Circumference: {c2.circumference()}")