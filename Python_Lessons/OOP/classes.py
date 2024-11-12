# class Human:
#     def __init__(self, name, age, hobby):
#         self.name = name
#         self.age = age
#         self.hobby = hobby

#     def eat(self):
#         '''Makes ahuman eat'''
#         return f'{self.name} is eating'
        
#     def speak(self):
#         '''Makes human speak'''
#         return f'{self.name} is speaking'
        
#     # def read(self):
#     #         '''Makes human read'''
#     #     return f'{self.name} is reading'
        
# human1 = Human("Precious", 21, 'Asking questions')
# human2 = Human("Priscilla", 24, 'Snapchatting')
# human3 = Human("Rhoda", 22, 'Reading')


# print(human1.eat())
# print(human2.speak())
# print(human3.read())


'''Make a class called restaurant
The __init__ method for restaurant should store two attributes, a restaurant name and a cuisine type
Make a method called describe restaurant that prints two pieces of information
And another method called open restaurant that prints a message
indicating that the restaurant is open
Mkae two instances from your restaurant class
Print two attributes individually and then call both methods'''

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
    
#     def describe_restaurant(self):
#         print(f'The name of this restaurant is {self.name}.')
#         print(f'They serve {self.cuisine_type} dishes.')

    
#     def open_restaurant(self):
#         return f'{self.name} restaurant is open.'
    
# restaurant1 = Restaurant('The Golden Tullip', 'Continental')
# restaurant2 = Restaurant('Dimaensa', 'Local')

# print(restaurant2.name)
# print(restaurant1.cuisine_type)

# print(restaurant1.describe_restaurant())
# print(restaurant2.open_restaurant())


'''Make a class acalled user
Create 2 attribute: first and lastname
And create several other attributes that are typically stored in a user profile
Make a method called describe user that prints a summary of the user's information
make another method called greet user that prints a personalized greeting to the user
Create several instances that represent different users and call both methods on each user
'''

# class User:
#     def __init__(self, firstname, lastname, age, student_satus, career, nationality):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.student_status = student_satus
#         self.career = career
#         self.nationality = nationality
    
#     def describe_user(self):
#         print(f'This user is caleed {self.firstname} {self.lastname}.')
#         print(f'She is {self.age} years old and a {self.student_status}')
#         print(f'She aspires to be a {self.nationality} {self.career}\n')

#     def greet_user(self):
#         return f'Hello {self.firstname} {self.lastname}. You are welcome!\n'
    
# user1 = User('Rhoda', 'Lee', 22, 'Student', 'Tech Enthusiast', 'Ghanaian')
# print(user1.greet_user())

# user2 = User('Antwiwaa', 'Conduah', 19, 'Student', 'Tech Enthusiast', 'Ghanaian')
# print(user2.describe_user())



'''Library Book Class

Create a class called Book.

Add attributes for title, author, publication_year, and genre.

Write a method called describe_book that prints a summary of the book's information.

Write another method called is_classic that returns True if the book was published before 1970, and False otherwise.

Create a few instances of Book and call both methods on each instance.'''

class Book:
    def __init__(self, title, author, publication_year: int, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
    
    def describe_book(self):
        return f'{self.title} is a {self.genre} book \nthat was written by {self.author} \nand published {self.publication_year}'
    
    def is_classic(self):
        if self.publication_year < 1970:
            print('This is a classic!')
            return True
        else:
            print('This is not a classic.')
            return False
        
book1 = Book('In The Middle of Nowhere', 'Ruby Yayra Goga', 2013, 'Mystery')
book2 = Book('Justify Your Inclusion', 'Samelia Bawuah', 1860, 'Adventure')

print(book1.genre)
print(book2.author)

print(book1.describe_book())
print(book2.is_classic())



'''Pet Class

Create a class called Pet.

Add attributes for name, animal_type, and age.

Write a method called describe_pet that prints a summary of the pet's information.

Write another method called age_in_dog_years that converts the pet's age to dog years (1 human year = 7 dog years).

Create a few instances of Pet and call both methods on each instance.'''

class Pet:
    def __init__(self, name, animal_type, age: int):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def describe_pet(self):
        return f'{self.name} is a {self.animal_type} that is {self.age} years old!'
    
    def age_in_dog_years(self):
        self.age = self.age * 7
        return f'{self.name}\'s age in dog years is {self.age}\n'
    
dog = Pet('Pluto', 'Dog', 2)
cat = Pet('Ginger', 'Cat', 4)

print(dog.describe_pet())
print(dog.age_in_dog_years())

print(cat.describe_pet())
print(cat.age_in_dog_years())

