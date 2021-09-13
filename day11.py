"""
Question 38:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half
values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""

def divideTuple():
    wholeTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(wholeTuple[0:5])
    print(wholeTuple[-5:])


divideTuple()

"""
Question 39:
Write a program to generate and print another tuple whose values are even numbers in the given tuple 
(1,2,3,4,5,6,7,8,9,10).

Hints:
Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.
"""

def printEvenNumbersFromTuple():
    wholeTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for _ in wholeTuple:
        if _ % 2 == 0:
            print(_)


printEvenNumbersFromTuple()