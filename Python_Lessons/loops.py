# #!/usr/bin/python3

# # For Loop

# items = (2, 4, 6, 8, 10, 12)

# # Break keyword in for loops
# print('Break keyword in for loops')
# for item in items:
#     if item == 8:
#         #print('Found 8')
#         break
#     print(item)


# # Continue keyword in for loops
# print('Continue keyword in for loops')
# for item in items:
#     if item == 8:
#         #print('Found 8')
#         continue
#     print(item)



# # Range function in for loops
# print('Range function in for loops')
# for item in range(11):
#     print(item)


# # Nested Loop
# print('Nested Loop')
# letters = "abcdef"
# for item in items:  # outer loop
#     for letter in letters:  # inner loop
#         print(item, letter)


# # Looping Throug a Tuple
# print('Looping through a tuple')
# my_tuple = ('a', 'b', 'c', 'd')

# for letter in my_tuple:
#     print(letter)



# # Looping Through Dictionaries
# print('Looping Through a Dictionary')
# my_dict = {
#     'name': 'Dede',
#     'age': 22,
#     'work': 'Sleeper',
#     'energy level': 43
# }

# for key, value in my_dict.items():
#     print(key, value)

# print(my_dict.items())

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)


'''
Dictionary called student with keys name age and city and corresponding values
Use a for loop to print each key value pair in the format, key: value using f string
'''
# student = {
#     'name': 'Dede',
#     'age': 22,
#     'city': 'Accra'
# }

# for key, value in student.items():
#     print(f'{key}: {value}')



'''
Create a list called grades containing 85 72 90 68 80
Use a for loop to print only grades that are above 80
Calculate and print the average of all grades
'''

# grades = [85, 72, 90, 68, 80]

# for grade in grades:
#     if grade > 80:
#         print(grade)

# total = sum(grades)
# length = len(grades)
# print(total / length)


'''
Create a list of tuples called products containing product names and prices:
products =[('Apple', 1.29),('bannana', 0.59), ('Orange', 0.79)]
Use a for loop to unpack each tupple and print 'Product: [name] - Price: [price]'
'''
# products = [('Apple', 1.29),('Bannana', 0.59), ('Orange', 0.79)]

# for name, price in products:
#     print(f'Product: {name} - Price: {price}')


'''
A while loop will run so long as a condition is true
'''

# current_number = 0

# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# break statement in while loops
# while current_number <= 10:
#     if current_number == 5:
#         print('I met 5')
#         break
#     print(current_number)
#     current_number += 1



# continue statement in while loops
# while current_number <= 10:
#     if current_number == 5:
#         print('I skipped 5')
#         current_number += 1
#         continue
#     print(current_number)
#     current_number += 1


# Infinite loop
# while True:
#     print(current_number)
#     current_number += 1

'''
Ask user to give a message and the message should keep on repeating until they press a particular key
"Tell me something and I'll repeat it"
'''

# prompt = 'Tell me something and I\'ll repeat it \nIt can be your name or anything you want.\n'


# message = ''
# while message != 'quit':
#     message = input(prompt)
#     #if message != 'quit':
#     print(f'\nYour message was: {message}')


'''
Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value
As they enter each topping print a message saying you'll add that topping to their pizza
'''
# prompt = 'What toppings would you want on your pizza?\n'

# message = ''

# while message != 'quit':
#     message = input(prompt)
    
#     print(f'\nWe will add that topping to your pizza: {message}')
#     mess_to_list = list(message)
#     print_mess = mess_to_list.append(message)
#     print(print_mess)
  
# Functions help to write reusable code
# def greet():
#     pass

# def greet_me():
#     print('Hello Student')

# greet_me()

# def greet_student(name):
#     print(f'Hello, {name}')

# greet_student('Dede')

#return keyword in functions 
#an executed function is equal to its return value
# This means that the excuted function is same as the return value
# Not all functions have a return value

'''
Write a function called display message that prints one sentence that tells everyone what you are learning
Call the function and make sure the mesage displays correctly
'''
def message(course):
    print(f'I am learning {course} with HACSA')

message('Backend Development')


'''
Write a function called favorite book that accepts one parameter called title
It should print a message telling everyone about your favorite book
'''

def favorite_book(title):
    print(f'I love horror themed novels and my favorite is {title} by R. L. Stine')

favorite_book('Hunted Lands')

   
    