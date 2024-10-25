my_set = {'Grace', 'Naomi', 'Emefa', 'Priscilla', 'Jennifer'}
print(my_set)

print('Grace' in my_set)

my_other_set = {'Naomi', 'Antwiwaa', 'Dede', 'Emefa'}

print(my_set.intersection(my_other_set)) # or use the '&' for intersection
print(my_set & my_other_set)

print(my_set.union(my_other_set)) # or use '|' for union
print(my_set | my_other_set)

print(my_set.difference(my_other_set)) # or use '-' for difference
print(my_set - my_other_set)

print(my_other_set.difference(my_set))
print(my_other_set - my_set)

# Convert a list to a set
numbers = [1, 5, 3, 8, 8, 5]

unique_numbers = set(numbers)
print(unique_numbers)

# Convert the new set back into a list, 
# note this doesn't bring back duplicates that were removed
new_list = list(unique_numbers)
new_list.sort()
print(new_list)

# creating an empty list, tuple and set
# var = list(var)
# var = tuple(var)
# var = set(var)

# list to set to tuple
# creating a list
a_list = ['Ama', 'Kofi', 'Adwoa', 'Afua', 3, 7, 2]
print(a_list)

# change list to tuple
a_tuple = tuple(a_list)
print(a_tuple)

# change the tuple to a set
a_set = set(a_tuple)
print(a_set)
a_set.add('Nabi')
print(a_set)
a_set.pop()
print(a_set)
# a_set.clear()
print(a_set)

print(dir(set))

#print(help(str.lower))
#print(help(list.reverse))
print(help(set.intersection))





