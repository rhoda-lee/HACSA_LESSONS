#!/usr/bin/python3

"""
1. my_string = 'Hello, T4Girls Backend'
Convert this to upper case, and then lower case

2. Print out how many times the letter 'e' occurs in that string

3. Return the first index of the 'Backend' in the entire string

4. Replace 'Backend' with 'Frontend' in that string

5. Concatenate these with f strings only!
name = 'Hi I am Priscilla.'
motivate = 'I am so excited and motivated to learn more Python,'
program = 'thanks to the HACSA foundation'

Expected Output: 'Hi I am Priscilla. I am so excited and motivated to learn more Python thanks to the HACSA foundation'


"""
my_string = "Hello, T4Girls Backend"
print(my_string.upper())

print(my_string.lower())

print(my_string.count("e"))

print(my_string.find("Backend"))

print(my_string.replace("Backend", "Frontend"))

name = "Hi! I am Priscilla."
motive = "I am so excited and motivated to learn more Python,"
program = "thanks to the HACSA foundation"

entire_greeting = f"{name} {motive} {program}"
print(entire_greeting)