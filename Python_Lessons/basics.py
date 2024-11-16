# # Strings
# # The hashtag is used for single line commenting in python
# # This is a comment

# '''The triple quotes is used
# for multiline commenting in python'''

# '''Strings are datatypes that are enclosed in quotation marks
# In python, a string can be enclosed in either single quotes or double quotes

# we discussed in our previous session that variables are containers that store data
# We use the assignment operator (=) to assign a value to a variable

# Variables can store any datatype.
# As we explore the string datatype, we'll have a look at how variables can be used to store strings.

# We'll also explore the string methods and how they are used to operate on strings
# Also, we'll'''

# first_name = 'Rhoda'
# last_name = 'Oduro-Nyarko'
# career = 'Tech Enthusiast'
# hobby = 'Disturbing my boyfriend and eating Indomie'

# fruits = ['Apples', 'Orange', 'Banana', 'Grape', 'Guava']

# #print("My name is " + first_name + " " + last_name)
# print(", ".join(fruits))

# print(last_name.replace('Oduro-Nyarko', 'Ninyung'))

# # .replace(string to replace, new replacement)

# print(f'My name is {first_name} {last_name}')



sentence = "Python is powerful and easy to learn."

print("Length of the string:", len(sentence))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Word 'powerful':", sentence[10:18])