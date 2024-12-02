# #!/usr/bin/python3

# # def create_album(number_of_songs, *songs):
# #     for song in songs:
# #         print(song)

# # create_album('Go Ahead', 'ME', 'Like You', 'Nights Like This')

# # def make_pizza(size, *toppings):
# #     #Making Pizza with a specific size
# #     print(f'\nMaking a {size}-inch pizza with the following toppings')

# #     for topping in toppings:
# #         print(f'- {topping}')

# # make_pizza(12, 'beef', 'chicken', 'pepporoni')

# # # Arbituary key-word or key-value arguments    - (*args) and (**kwargs)
# # def build_user(first_name, last_name, **user_info): # The two ** makes it a dictionary instead of a tupple
# #     user_info['firstName'] = first_name
# #     user_info['lastName'] = last_name
# #     return user_info

# # new_user = build_user('Rhoda', 'Lee', location = 'Accra', Institution = 'HACSA Tech4Girls')
# # print(new_user)


# '''
# Build a profile of yourself using your first and last name and 3 other value pairs that describe you
# Your function should return a dictionary
# '''

# def my_profile(first_name, last_name, **more_info):
#     more_info['FirstName'] = first_name
#     more_info['LastName'] = last_name
#     return more_info

# about_me = my_profile('Rhoda', 'Lee', Age = 22, Nationality = 'Ghanaian', Hobby = 'Reading')
# print(about_me)









'''Functions'''
'''A block of code that performs a specific action action'''
# def pen():
#     print('Writing with a pen')

# pen()

# def greet():
#     print('Hello!')

# greet()

# def greeting(name, height=0):
#     return f'Hello {name}, you are {height} cm'

# greeting('Rhoda', 168)



'''OOP is a programming paradigm, simply a way of writing code.'''

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_name(self):
        return f'Name: {self.name}'
    
    def age_in_ten_years(self):
        return self.age + 10
    
    # def __str__(self):
    #     return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


    def __repr__(self):
        return f'Human with name {self.name} is {self.age} years old and of gender {self.gender}'
    

human1 = Human('Augustine', 22, 'Female')

print(human1.age)
print(human1.gender)
print(human1.name)


print(human1.display_name())

print(human1)


