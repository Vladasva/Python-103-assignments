"""
Question 44:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:
Use map() to generate a list. Use lambda to define anonymous functions.
"""

def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1, 21)))
print(squaredNumbers)

"""
Question 45:
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this 
https://realpython.com/instance-class-and-static-methods-demystified/.
"""

class American:
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()

"""
Question 46:
Define a class named American and its subclass NewYorker.

Hints:
Use class Subclass(ParentClass) to define a subclass.*
"""

class American:
    @staticmethod
    def printNationality():
        print("I am American")

class NewYorker(American):
    pass


american = American()
newYorker = NewYorker()

print(american)
print(newYorker)