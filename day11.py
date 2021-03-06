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

"""
Question 40:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise 
print "No".

Hints:
Use if statement to judge condition.
"""

def printYes():
    stringInput = input("Enter any string: ")
    if stringInput.upper() == "YES":
        print("Yes")
    else:
        print("No")


printYes()

"""
Question 41:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.Use lambda to define anonymous functions.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squaredNumbers = map(lambda number: number ** 2, numbers)
print(list(squaredNumbers))

"""
Question 42:
Write a program which can map() and filter() to make a list whose elements are square of even number in 
[1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = filter(lambda number: number % 2 == 0, numbers)

squaredNumbers = map(lambda number: number ** 2, evenNumbers)
print(list(squaredNumbers))

"""
Question 43:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:
Use filter() to filter elements of a list. Use lambda to define anonymous functions.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

evenNumbers = filter(lambda number: number % 2 == 0, numbers)
print(list(evenNumbers))
