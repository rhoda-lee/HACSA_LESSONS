#!/usr/bin/python3

def make_pizza(size, *toppings):
    #Making Pizza with a specific size
    print(f'\nMaking a {size}-inch pizza with the following toppings')

    for topping in toppings:
        print(f'- {topping}')

#make_pizza(12, 'beef', 'chicken', 'pepporoni')

def destroy_pizza(size, *toppings):
    #Making Pizza with a specific size
    print(f'\nMaking a {size}-inch pizza with the following toppings')

    for topping in toppings:
        print(f'- {topping}')

def change_pizza(size, *toppings):
    #Making Pizza with a specific size
    print(f'\nMaking a {size}-inch pizza with the following toppings')

    for topping in toppings:
        print(f'- {topping}')