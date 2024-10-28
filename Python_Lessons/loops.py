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
student = {
    'name': 'Dede',
    'age': 22,
    'city': 'Accra'
}

for key, value in student.items():
    print(f'{key}: {value}')