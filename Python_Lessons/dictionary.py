'''
Dictionaries as a data type

They are also represented by curly braces but they appear in key value pairs
The key is the unique identifier to the value

'''


# Dictionary
my_dict = {'name': 'Rhoda',
           'age': 22,
           'program': 'Tech4Girls'
           }
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['program'])
print(my_dict)
#print(dir(dict))

print(my_dict.keys())
print(my_dict.values())

print(my_dict.get('program'))

# Add to dictionary
my_dict['coursemate'] = 'Antwiwaa'
print(my_dict.get('coursemate'))

# Override or change a value
my_dict['name'] = 'Rhoda Lee'
print(my_dict['name'])
my_name = my_dict['name']
print(f'my name is {my_name}')

# Deleting a key value pair
del my_dict['coursemate']
print(my_dict)

my_dict.pop('program') # takes an argument which is they key in order to pop a value
print(my_dict)

# To update multiple key value pairs
my_dict.update({'name': 'Dede',
                'age': 23,
                'program': 'ALX',
                'country': 'Ghana',
                'coursemate': 'Nana Afua'
                })

print(my_dict)



 




