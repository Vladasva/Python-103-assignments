"""
Question 22:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key
alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def checkFrequency():
    uniqueValues = []
    sentence = input("Enter any sentence: ").split()

    sentence.sort()

    for word in sentence:
        if word not in uniqueValues:
            uniqueValues.append(word)

    for uniqueWord in uniqueValues:
         print(uniqueWord, ":", sentence.count(uniqueWord))


checkFrequency()

"""
Question 23:
Write a method which can calculate square value of number

Hints:
Using the ** operator which can be written as n**p where means n^p
"""

def square():
    while True:
        try:
            number = int(input("Enter any number: "))
            print(number**2)
            break
        except:
            print("Please, enter a number!")


square()