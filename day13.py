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

"""
Question 49:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as 
argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints
To override a method in super class, we can define a method with the same name in the super class.
"""

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


Asqr = Square(5)
print(Asqr.area())

print(Square().area())

"""
Question 50;
Please raise a RuntimeError exception.

Hints
Use raise() to raise an exception.

"""

raise RuntimeError('something wrong')
