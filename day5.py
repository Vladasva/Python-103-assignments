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
            squaredNumbers.append(str(number**2))

    print(", ".join(squaredNumbers))


squareEachOddNumber()

"""
Question 17:
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def calculateBalance():
    balance = 0
    while True:
        transaction = str(input("Please, enter 'D' for deposit, 'W' for withdrawal and the sum or 'Q' to stop: "))
        if transaction[0].upper() == 'D':
            sum = int(transaction[1:])
            balance += sum
        elif transaction[0].upper() == 'W':
            sum = int(transaction[1:])
            balance -= sum
        elif transaction.upper() == 'Q':
            break
    print(balance)


calculateBalance()