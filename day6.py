"""
Question 18:
A website requires the users to input username and password to register. Write a program to check the validity of
password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def checkPasswords():
    passwords = input("Please, enter some passwords: ")
    passwords = passwords.split(", ")
    correctPassword = []
    for password in passwords:
        if 6 <= len(password) <= 12:
            if any(chr.isdigit() for chr in password):
                if any(chr1.isalpha() for chr1 in password):
                    if any(chr2.islower() for chr2 in password):
                        if any(chr3.isupper() for chr3 in password):
                            if any(chr4 == "$" or chr4 == "#" or chr4 == "@" for chr4 in password):
                                correctPassword.append(password)
            else:
                print("Any of passwords are not correct.")

    print(", ".join(correctPassword))


checkPasswords()

"""
Question 19:
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age 
and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.We use itemgetter to 
enable multiple sort keys.
"""

from operator import itemgetter


def sortNameAgeScore():
    lines = []
    tuplesList = []
    while True:
        s = input("Enter the name, age and score, press ENTER for new line, enter empty string to see output: ")
        if s:
            lines.append(s)
        else:
            break

    for line in lines:
        tuplesLine = tuple(map(str, line.split(",")))
        tuplesList.append(tuplesLine)

    print(sorted(tuplesList, key=itemgetter(0, 1, 2)))


sortNameAgeScore()