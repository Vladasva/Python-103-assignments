"""
Question 10:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.We use set container
to remove duplicated data automatically and then use sorted() to sort the data.
"""

def someFunction():
    words = input("Please, enter some text: ")
    words = words.split(" ")
    filtered = []
    for word in words:
        if word not in filtered:
            filtered.append(word)
            filtered.sort()
    print(" ".join(filtered))


someFunction()

"""
Question 11:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def divisibleByFive():
    divisibleFive = []
    numbers = input("Please, enter 4 digits binary numbers, separated by comma: ")
    numbers = numbers.split(",")
    for number in numbers:
        if int(number, 2) % 5 == 0:
            divisibleFive.append(number)

    print(", ".join(divisibleFive))


divisibleByFive()

"""
Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def foundEven():
    evenNumbers = []
    for number in range(1000, 3001):
        if int(number) % 2 == 0:
            evenNumbers.append(str(number))

    print(", ".join(evenNumbers))


foundEven()