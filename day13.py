"""
Question 47:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the
area.

Hints
Use def methodName(self) to define a method.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * (self.radius ** 2)


circle = Circle(5)
print(circle.area())

"""
Question 48:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which 
can compute the area.

Hints
Use def methodName(self) to define a method.
"""

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(4, 5)
print(rectangle.area())