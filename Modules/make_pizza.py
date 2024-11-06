#!/usr/bin/python3

# import pizza #This imports the entire module
# from pizza import * #Imports all functions in the module

# from pizza import make_pizza as mp, change_pizza as cp

# mp(12, 'beef', 'chicken', 'ham')

# from pizza import make_pizza as mk

# mk(12, 'Ham', 'Sausage', 'Beef')
import math
import os

# print(math.pi)
# #help(math)

# print(os.getcwd())
# #os.mkdir('test_dir')
# print(os.listdir("."))

#import random # for random numbers and sequences
import random
random_number = random.randint(1, 20) # prints a random integer
print(random_number)

print(random.random()) #prints random float

#choice function in random module
fruits = ['Apple', 'Mango', 'Strawberry', 'Banana']
print(random.choice(fruits))


# datetime module
#Syntax
    #module.class.funtion

import datetime
now = datetime.datetime.now()
print(now)
#print specific part of datetime

print(now.year)
print(now.month)
print(now.day)
print(now.time)
print(now.date)



