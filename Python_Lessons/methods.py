# Question
'''
1. Create a list callsed numbers containing the numbers 1,3,5 & 8
Append number "10" to the end of the list
Insert "2" at index 1
remove "3" from the list
Print the final list

2. create a list called colors containing the colors 'red', 'green', 'blue', 'yellow', 'purple'
Sort the list alphabetically 
Reverse the sorted list
Print the final list

3. Create a list call temperatures containing 25, 18, 32, 20, 28
Find the min, max temperature
Print both values

4. Create a list called scores containing 85, 72, 90, 68, 80
calculate the total sum of the scores and print the total sum

5. Create a list called animals containing 'cat', 'dog', 'bird', 'fish'
Remove the element at index 2
Replace the element at index 1 with lizard
Use pop to remove and return the last element
Print the final list

6. Create two list list1 =[1,2,3] list2 = [4, 5, 6]
Combine list2 into list1 and print the final list

7. Create a list called names containing ['Alice', 'Bob', 'Charlie', 'David']
Find the index of Bob and print out the index of Bob



'''

# Question 1
numbers = [1, 3, 5, 8]

numbers.append(10)
numbers.insert(1, 2)
numbers.remove(3)

print(numbers)

# Question 2
colors = ['red', 'green', 'blue', 'yellow', 'purple']
colors.sort()

colors.sort(reverse=True)
print(colors)

# Question 3
temperature = [25, 18, 32, 20, 28]
max_temp = max(temperature)
print(max_temp)
min_temp = min(temperature)
print(min_temp)


# Question 4
scores = [85, 72, 90, 68, 80]
total = sum(scores)
print(total)

# Question 5
animals = ['cat', 'dog', 'bird', 'fish']
animals.remove('bird')
print(animals)
animals.insert(1, 'lizard')
popped = animals.pop()
print(popped)
print(animals)


# Question 6
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)

# Question 7
names = ['Alice', 'Bob', 'Charlie', 'David']
print(names.index('Bob'))