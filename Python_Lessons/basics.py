# # # # Strings
# # # # The hashtag is used for single line commenting in python
# # # # This is a comment

# # # '''The triple quotes is used
# # # for multiline commenting in python'''

# # # '''Strings are datatypes that are enclosed in quotation marks
# # # In python, a string can be enclosed in either single quotes or double quotes

# # # we discussed in our previous session that variables are containers that store data
# # # We use the assignment operator (=) to assign a value to a variable

# # # Variables can store any datatype.
# # # As we explore the string datatype, we'll have a look at how variables can be used to store strings.

# # # We'll also explore the string methods and how they are used to operate on strings
# # # Also, we'll'''

# # # first_name = 'Rhoda'
# # # last_name = 'Oduro-Nyarko'
# # # career = 'Tech Enthusiast'
# # # hobby = 'Disturbing my boyfriend and eating Indomie'

# # # fruits = ['Apples', 'Orange', 'Banana', 'Grape', 'Guava']

# # # #print("My name is " + first_name + " " + last_name)
# # # print(", ".join(fruits))

# # # print(last_name.replace('Oduro-Nyarko', 'Ninyung'))

# # # # .replace(string to replace, new replacement)

# # # print(f'My name is {first_name} {last_name}')



# # sentence = "Python is powerful and easy to learn."

# # print("Length of the string:", len(sentence))
# # print("First character:", sentence[0])
# # print("Last character:", sentence[-1])
# # print("Word 'powerful':", sentence[10:18])



# '''-------- PLEASE WORK ON THESE EXERCISES WHEN YOU JOIN THE MEETING ------'''

# '''Write a separate program to accomplish each of these exercises. Save each program with a filename that follows standard Python conventions, using lowercase
# letters and underscores, such as simple_message.py and simple_messages.py.
# 2-1. Simple Message: Assign a message to a variable, and then print that
# message.
# 2-2. Simple Messages: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new
# message.'''


# '''2-3. Personal Message: Use a variable to represent a person's name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
# 2-4. Name Cases: Use a variable to represent a person's name, and then print
# that person's name in lowercase, uppercase, and title case.'''
# #: Use title() for title case I will explain exactly what it does

# # languages: str = print(" Languages: \n\tPython \n\tJava \n\tC++ \n\tRuby")
# # stripped = languages.strip()
# # print(stripped)

# # message = 'Hello you\'re welcome'
# # print(message)

# # num1 = 4
# # num2 = 5

# # #Addition (+)
# # add = num1 + num2 
# # print(f'The sum of {num1} and {num2} is {add}')

# # #Subtraction (-)
# # print(num1 - num2)

# # #Multiplication (*)
# # print(num1 * num2)

# # #Division (/)
# # print(num1 / num2)

# # #Exponentiation (**)
# # print(num1 ** num2)

# # #Modulos (%)
# # x = 4
# # y = 3
# # # print(x / y)
# # # print(x % y)

# # # Floor Division (//)
# # print(x // y)

# # '''BODMAS
# #    PEDMAS
# #    BEDMAS'''

# # (x + y) * 2 ** 3

# # # Using underscores in numbers
# # number = 120_245_342_000_000_000
# # print(number)

# # x, y, z = 1, 2, 3
# # print(x)

# # PI = 3.142

# # #print(dir(str))
# # print(dir(list))

# fruits = ['Apple', 'Orange', 'Pineapple', 'Mango']
# print(fruits)
# print(len(fruits))

# # Adding an element to a list .append()
# fruits.append('Guava')
# print(fruits)

# # Removing an element from a list .remove()
# fruits.remove('Apple')
# print(fruits)

# # removing last element in a list .pop()
# fruits.pop()
# print(fruits)

# # Reversing the list .reverse()
# fruits.reverse()
# print(fruits)

# # Accessing elements in a list by their index
#     #Use the square bracket notation
# print(fruits[0])

# print(fruits[-1])

# # Inserting an element into a list
# fruits.insert(0, 'Apple')
# print(fruits)


# arr = [1, 2, 3, 4, 5]

def left_rotate(n, arr):
    rotated_array = arr[n:] + arr[:n]
    return rotated_array

print(left_rotate(4, [1, 2, 3, 4, 5]))

def insertTail(node, tail):
    current = tail

    while current:
        tail.append(node)