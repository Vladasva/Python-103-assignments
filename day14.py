"""
Question 51;
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints
Use try/except to catch exceptions.
"""

def computeZeroFromFive():
    try:
        return 5/0
    except ZeroDivisionError:
        print("Do not divide by zero!")


computeZeroFromFive()



