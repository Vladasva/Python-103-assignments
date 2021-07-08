"""
4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
which contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

def listTupleGenerator():
    numberSequence = input('Enter sequence of numbers separated by comma: ')
    listedSequence = numberSequence.split(",")

    print(listedSequence)
    print(tuple(listedSequence))


listTupleGenerator()

"""
5. Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
"""

class twoMethods:

    def getString(self):
        while True:
            try:
                self.text = input('Enter some text: ')
                return self.text
                break
            except:
                print("Please enter text")

    def printString(self):
        self.capitalizedText = self.text.upper()
        return print(self.capitalizedText)

someText = twoMethods()
someText.getString()
someText.printString()

"""
6. Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume 
the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output
received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it should be
assumed to be a console input.
"""

import math

def calculatesFormula():
    result = []
    D = input("Enter three numbers separated by comma: ")
    D = D.split(",")
    for _ in D:
        C = 50
        H = 30
        Q = math.sqrt((2 * C * int(_))/H)
        Q = int(Q)
        result.append((str(Q)))

    str1 = ','.join(result)
    print(str1)


calculatesFormula()

"""
7. Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a 
comma-separated form.
"""

import numpy as np

def arrayGenerator():
    numbers = input('Please, enter two numbers via comma: ')
    numbers = numbers.split(",")
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    numbers = tuple(numbers)
    rows, cols = numbers
    arr = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(j)
        arr.append(col)
    arr1 = np.array(arr)
    arr2 = []
    for l in range(len(arr1)):
         arr2.append(((arr1[l] * l).tolist()))
    print(arr2)


arrayGenerator()

"""
Question 8:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
"""

def sortAlphabetically():
    words = str(input("Please enter words separating them by comma: "))
    words = words.split(",")
    words.sort()
    print(", ".join(words))


sortAlphabetically()

"""
Question 9:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def capitalizeLines():
    lines = []
    while True:
        s = input("Enter the string or press ENTER for new line, enter empty string to see output: ")
        if s:
            lines.append(s)
        else:
            break

    print("OUTPUT: ")
    for i in lines:
        print(i.upper())


capitalizeLines()