#!/usr/bin/python3

# name = input('What is your name?: ')
# age = float(input('What is your age?: '))
# amount = float(input('How much do you have in your account?: '))
# print(f'Your name is {name} and you are {age} years old and your balance is {amount}!')

# age = age + 1
# amount = amount * 2


# prompt = f'Hello {name} welcome to my script!'
# prompt += '\nDo you want to say more? '

# message = input(prompt)

'''
Determine if a user can go to university based on their age
if the user is 18 or older, print "You are old enought to enroll"
else print "You will be able to enroll when you are a little older"
'''

'''age = int(input('How old are you?: '))

if age >= 18:
    print('\nYou are old enough to enroll')
else:
    print('\nYou will be able to enroll when you are a little older')'''


'''
Write a program that asks the user what kind of rental car they would like
Print a message about the car such as "Let me see if I can find you a {name of car}"
'''

# car_type = input('What kind of car would you like to rent?: \n')

# print(f'Let me see if I can find you a {car_type} with a door')


'''
Write a program that asks the user how many people are in their dinner group
If the answer is more than 8, print  MESSAGE SAYING " tHEY'll have to wait for a table"
Otherwise report that their table is ready
'''

number_in_group = int(input('how many people are in your dinner group?: \n'))

if number_in_group > 8:
    print('You will have to wait for a table')
else:
    print('Your table is ready!')