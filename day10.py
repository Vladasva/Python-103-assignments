"""
Question 31:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for
loops.
"""

def squareDictionaryOneToTwenty():
    squaredOneToTwenty = {}
    for _ in range(1, 20):
        if _ > 0:
            squaredOneToTwenty[_] = (_ ** 2)

    print(squaredOneToTwenty)


squareDictionaryOneToTwenty()