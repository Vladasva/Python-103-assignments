"""
Question 31:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for
loops.
"""

def squareDictionaryOneToTwenty():
    squaredOneToTwenty = {}
    for _ in range(1, 20+1):
        if _ > 0:
            squaredOneToTwenty[_] = (_ ** 2)

    print(squaredOneToTwenty)


squareDictionaryOneToTwenty()

"""
Question 32:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys. The function should just print the keys only.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for 
loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""

def squareDictionaryOneToTwenty():
    squaredOneToTwenty = {}
    for _ in range(1, 20+1):
        if _ > 0:
            squaredOneToTwenty[_] = (_ ** 2)

    print(squaredOneToTwenty.keys())


squareDictionaryOneToTwenty()

"""
Question 33:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both
included).

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.
"""

def squareListOneTwoTwenty():
    squaredListOneTwoTwenty = []
    for _ in range(1, 21):
        squaredListOneTwoTwenty.append(_ ** 2)

    print(squaredListOneTwoTwenty)


squareListOneTwoTwenty()

"""
Question 34:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] 
to slice a list
"""

def squareListOneTwoTwenty():
    squaredListOneTwoTwenty = []
    for _ in range(1, 21):
        squaredListOneTwoTwenty.append(_ ** 2)

    print(squaredListOneTwoTwenty[0:5])


squareListOneTwoTwenty()

"""
Question 35:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.

Hints: 
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use 
[n1:n2] to slice a list
"""

def squareListOneTwoTwenty():
    squaredListOneTwoTwenty = []
    for _ in range(1, 21):
        squaredListOneTwoTwenty.append(_ ** 2)

    print(squaredListOneTwoTwenty[-5:])


squareListOneTwoTwenty()

"""
Question 36:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.

Hints: 
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""

def squareListOneTwoTwenty():
    squaredListOneTwoTwenty = []
    for _ in range(1, 21):
        squaredListOneTwoTwenty.append(_ ** 2)

    print(squaredListOneTwoTwenty[6:21])


squareListOneTwoTwenty()

"""
Question 37:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 
(both included).

Hints: 
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use
tuple() to get a tuple from a list.
"""

def printTuple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))


printTuple()