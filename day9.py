"""
Question:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
"""

def sumOfTwoNumber(number1, number2):
    return print(number1 + number2)


sumOfTwoNumber(30, 45)

"""
Question 27:
Define a function that can convert a integer into a string and print it in console.

Hints:
Use str() to convert a number to string.
"""

def convertItnToString(number):
    numberString = str(number)
    return print(numberString)


convertItnToString(5)

"""
Question 28:
Define a function that can receive two integer numbers in string form and compute their sum and then print it in 
console.

Hints:
Use int() to convert a string to integer.
"""

sumNumbers = lambda s1, s2: int(s1) + int(s2)
print(sumNumbers("5", "3"))

"""
Question 29: 
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:
Use + sign to concatenate the strings.
"""

concatenateStrings = lambda s1, s2: s1 + s2
print(concatenateStrings("5", "3"))

"""
Question 30:
Define a function that can accept two strings as input and print the string with maximum length in console. If two
strings have the same length, then the function should print all strings line by line.

Hints:
Use len() function to get the length of a string.
"""

def checkStringLength(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 == len2:
        print(string1)
        print(string2)
    elif len1 > len2:
        print(string1)
    elif len1 < len2:
        print(string2)


checkStringLength("Yes", "No")
