#!/usr/bin/python3

# def create_album(number_of_songs, *songs):
#     for song in songs:
#         print(song)

# create_album('Go Ahead', 'ME', 'Like You', 'Nights Like This')

# def make_pizza(size, *toppings):
#     #Making Pizza with a specific size
#     print(f'\nMaking a {size}-inch pizza with the following toppings')

#     for topping in toppings:
#         print(f'- {topping}')

# make_pizza(12, 'beef', 'chicken', 'pepporoni')

# # Arbituary key-word or key-value arguments    - (*args) and (**kwargs)
# def build_user(first_name, last_name, **user_info): # The two ** makes it a dictionary instead of a tupple
#     user_info['firstName'] = first_name
#     user_info['lastName'] = last_name
#     return user_info

# new_user = build_user('Rhoda', 'Lee', location = 'Accra', Institution = 'HACSA Tech4Girls')
# print(new_user)


'''
Build a profile of yourself using your first and last name and 3 other value pairs that describe you
Your function should return a dictionary
'''

def my_profile(first_name, last_name, **more_info):
    more_info['FirstName'] = first_name
    more_info['LastName'] = last_name
    return more_info

about_me = my_profile('Rhoda', 'Lee', Age = 22, Nationality = 'Ghanaian', Hobby = 'Reading')
print(about_me)