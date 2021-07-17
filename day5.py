"""
Question 16:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated
numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def squareEachOddNumber():
    squaredNumbers = []
    sequence = input("Please, enter sequence of numbers separated by comma: ")
    sequence = sequence.split(",")
    for number in sequence:
        number = int(number)
        if number % 2 != 0:
            squaredNumbers.append(number**2)

    print(squaredNumbers)


squareEachOddNumber()