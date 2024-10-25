#!/usr/bin/python3

my_string = 'Hello Control Flow'

#If Statements
if my_string == 'Hello Control Flow':
    print(True)

# If else statements
if my_string == 'Hello Control Flow':
    print(True)
else:
    print(False)

# If, else and elif statements
if my_string == 'Hello Control Flow':
    print(True)
elif my_string != 'Hello Control Flow':
    print(False)
else:
    print("What is going on here?")

my_set = {1, 3, 6, 8}

if 4 in my_set:
    print("Inclusive")
else:
    print("Exclusive")

if 4 | 2 in my_set:
    print("Inclusive")
else:
    print("Exclusive")

if (4 & 6) in my_set:
    print("Inclusive")
else:
    print("Exclusive")


    # Number is 7
    # If number is div by 2 print number is even else number is odd
number = 7

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")