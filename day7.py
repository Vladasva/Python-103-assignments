"""
Question 20:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
Hints:
Consider use class, function and comprehension.
"""

class Divisible:

    def bySeven(self, n):
        for number in range(0, 1 + n):
            if number % 7 == 0:
                yield number


divisible = Divisible()
generator = divisible.bySeven(int(input("Please enter number: ")))
for number in generator:
    print(number)

"""
Question 21:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after
a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If
the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.Here distance 
indicates to euclidean distance.Import math module to use sqrt function.
"""

import math

def findPosition():
    lines = []
    tuplesList = []
    x = 0
    y = 0

    while True:
        s = input("Enter 'UP', 'DOWN', 'RIGHT' and 'LEFT' and number: ")
        if s:
            lines.append(s)
        else:
            break

    for line in lines:
        tuplesLine = tuple(map(str, line.split(" ")))
        tuplesList.append(tuplesLine)

    if str(tuplesList[0][0].upper()) == 'UP':
        y += int(tuplesList[0][1])
    if tuplesList[1][0].upper() == 'DOWN':
        y -= int(tuplesList[1][1])
    if tuplesList[2][0].upper() == 'RIGHT':
        x += int(tuplesList[2][1])
    if tuplesList[3][0].upper() == 'LEFT':
        x -= int(tuplesList[3][1])

    distance = round(math.sqrt((x**2) + (y**2)))

    print(distance)


findPosition()