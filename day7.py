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
