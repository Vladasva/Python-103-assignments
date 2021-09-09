"""
Question 31:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for
loops.
"""

# def squareDictionaryOneToTwenty():
#     squaredOneToTwenty = {}
#     for _ in range(1, 20+1):
#         if _ > 0:
#             squaredOneToTwenty[_] = (_ ** 2)
#
#     print(squaredOneToTwenty)
#
#
# squareDictionaryOneToTwenty()

"""
Question 32:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
values are square of keys. The function should just print the keys only.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for 
loops.Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
"""

# def squareDictionaryOneToTwenty():
#     squaredOneToTwenty = {}
#     for _ in range(1, 20+1):
#         if _ > 0:
#             squaredOneToTwenty[_] = (_ ** 2)
#
#     print(squaredOneToTwenty.keys())
#
#
# squareDictionaryOneToTwenty()

"""
Question 33:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both
included).

Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.
"""

def squareListOneTwoTwenty():
    squaredListOneTwoTwenty = []
    for _ in range(1, 21):
        squaredListOneTwoTwenty.append(_ ** 2)

    print(squaredListOneTwoTwenty)

squareListOneTwoTwenty()
