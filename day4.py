"""
Question 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def countsUpperLower():
    upper = []
    lower = []
    sentence = input("Enter any sentence: ")
    for symbol in sentence:
        if symbol.isupper():
            upper.append(symbol)
        elif symbol.islower():
            lower.append(symbol)

    print("UPPER CASE", len(upper))
    print("LOWER CASE", len(lower))


countsUpperLower()