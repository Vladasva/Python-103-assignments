"""
Question 54:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
company name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com
Then, the output of the program should be:

google
In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use \w to match letters.
"""

# import re
#
# def printDomain():
#     email = str(input("Please, enter some email: "))
#     pattern = "\w+@(\w+).com"
#     domain = re.findall(pattern, email)
#     print(domain)
#
#
# printDomain()

"""
Question 55:
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits
only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.

Hints
Use re.findall() to find all substring using regex.
"""

# import re
#
# def printNumbers():
#     sentence = str(input("Please, enter some text with numbers: "))
#     pattern = "\d+"
#     numbers = re.findall(pattern, sentence)
#     print(numbers)
#
#
# printNumbers()

"""
Question 56:
Print a unicode string "hello world".

Hints
Use u'strings' format to define unicode string.
"""

# unicodeString = u"hello world"
# print(unicodeString)

"""
Question 57:
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints
Use unicode()/encode() function to convert.
"""

s = input()
u = s.encode('utf-8')
print(u)