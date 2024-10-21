#!/usr/bin/python3

x = 4
print(x)

# This is a comment

"""
This is my multiline comment for my code
This is also for my class

"""
# message = "Hello World \"I am a girl\""
# name = 'Naomi\'s Food Court'
# print(message)
# print(len(message))
# print(message[:11])
# print(message.lower())
# print(message.upper())
# print(message.count('l'))
# print(message.find('o'))

# print(message.replace('World', 'Universe'))

### STRING CONCATENATION

user = "Dede"
greeting ="Welcome"
more_greeting = "to the Backend class"

print(greeting + ' ' + user + ', ' + more_greeting)

# Formatted strings
entire_greeting = "{} {}, {}".format(greeting, user, more_greeting)
print(entire_greeting)

# f"{}" strings
entire_greeting = f'{greeting} {user.upper()} {more_greeting.upper()}'
print(entire_greeting)


