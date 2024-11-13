# class Human:
#     def __init__(self, firstname, lastname, age, hobby):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.hobby = hobby

#     def eat(self):
#         '''Makes ahuman eat'''
#         return f'{self.name} is eating'

#     def set_middle_name(self, middle_name):
#         if middle_name:
#             self.middle_name = middle_name
    
#     def display_full_name(self):
#         if self.middle_name:
#             return f'{self.firstname} {self.middle_name} {self.lastname}'
#         else:
#             return f'{self.firstname} {self.lastname}'
        
# human1 = Human("Precious", 21, 'Asking questions')
# human2 = Human("Priscilla", 24, 'Snapchatting')
# human3 = Human("Rhoda", 22, 'Reading')


# print(human1.eat())
# print(human2.speak())
# print(human3.read())

# # Updating Instance Attributes with Dot Annotation
# human2.lastname = 'Adongo'

# # Updating Instances with instance methods
# human1.set_middle_name('Dede')
# print(human1.display_full_name())


'''Make a class called restaurant
The __init__ method for restaurant should store two attributes, a restaurant name and a cuisine type
Make a method called describe restaurant that prints two pieces of information
And another method called open restaurant that prints a message
indicating that the restaurant is open
Make two instances from your restaurant class
Print two attributes individually and then call both methods'''


'''
Add an attribute called number served with a default value of 0
Create an instance called restaurant from this class
Print the number of customers the restaurant has served then
change this value(number of customers served) and print it again
Add a method called set_number_served that lets you set the number of customers that have been served
Call this method with a new number and print the value again(Use instance method)'''

# class Restaurant:
#     def __init__(self, name, cuisine_type, number_served = 0):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = number_served
    
#     def describe_restaurant(self):
#         print(f'The name of this restaurant is {self.name}.')
#         print(f'They serve {self.cuisine_type} dishes.')

#     def open_restaurant(self):
#         return f'{self.name} restaurant is open.'
    

#     def set_number_served(self, new_number_served):
#         if new_number_served:
#             self.new_number_served = new_number_served

#     def display_number_served(self):
#         if self.new_number_served:
#             return f'{self.name} has served {self.new_number_served} people'
#         else:
#             return f'{self.name} has not served anyone!'
    
# restaurant1 = Restaurant('The Golden Tullip', 'Continental')
# restaurant2 = Restaurant('Dimaensa', 'Local')

# print(restaurant2.name)
# print(restaurant1.cuisine_type)

# print(restaurant1.describe_restaurant())
# print(restaurant2.open_restaurant())

# restaurant = Restaurant('Agyiwa\'s Kitchen', 'Local')
# print(restaurant.number_served)

# restaurant.number_served = 20
# print(f'The restaurant has now served: {restaurant.number_served} customers')


# prompt = int(input('Enter new number served: '))
# restaurant.set_number_served(prompt)
# print(restaurant.display_number_served())


'''Make a class called user
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

# class Book:
#     def __init__(self, title, author, publication_year: int, genre):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.genre = genre
    
#     def describe_book(self):
#         return f'{self.title} is a {self.genre} book \nthat was written by {self.author} \nand published {self.publication_year}'
    
#     def is_classic(self):
#         if self.publication_year < 1970:
#             print('This is a classic!')
#             return True
#         else:
#             print('This is not a classic.')
#             return False
        
# book1 = Book('In The Middle of Nowhere', 'Ruby Yayra Goga', 2013, 'Mystery')
# book2 = Book('Justify Your Inclusion', 'Samelia Bawuah', 1860, 'Adventure')

# print(book1.genre)
# print(book2.author)

# print(book1.describe_book())
# print(book2.is_classic())



'''Pet Class

Create a class called Pet.

Add attributes for name, animal_type, and age.

Write a method called describe_pet that prints a summary of the pet's information.

Write another method called age_in_dog_years that converts the pet's age to dog years (1 human year = 7 dog years).

Create a few instances of Pet and call both methods on each instance.'''

# class Pet:
#     def __init__(self, name, animal_type, age: int):
#         self.name = name
#         self.animal_type = animal_type
#         self.age = age

#     def describe_pet(self):
#         return f'{self.name} is a {self.animal_type} that is {self.age} years old!'
    
#     def age_in_dog_years(self):
#         self.age = self.age * 7
#         return f'{self.name}\'s age in dog years is {self.age}\n'
    
# dog = Pet('Pluto', 'Dog', 2)
# cat = Pet('Ginger', 'Cat', 4)

# print(dog.describe_pet())
# print(dog.age_in_dog_years())

# print(cat.describe_pet())
# print(cat.age_in_dog_years())



'''Bank Account Class

Create a class called BankAccount.

Add attributes for account_number, account_holder, and balance.

Write a method called display_balance that prints the account balance.

Write another method called deposit that increases the balance by a specified amount.

Write another method called withdraw that decreases the balance by a specified amount.

Create a few instances of BankAccount and call all methods on each instance.'''

# class BankAccount:
#     def __init__(self, account_number, account_holder, balance: float):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
    
#     def display_balance(self):
#         return self.balance
    
#     def withdraw(self, amount):
#         #amount: float
#         self.balance = self.balance - amount
#         return self.balance

# account1 = BankAccount('1234', 'Rhoda Oduro-Nyarko', 3000.00)
# account2 = BankAccount('5678', 'Augustine Ninyung', 5000.00)

# print(account1.display_balance())
# print(account1.withdraw(700))

# print(account2.display_balance())
# print(account2.withdraw(1500))


# Class Variables
'''They are variables that are shared between all the intances of that class
They do not change, they are always the same. Unlike instance variable that are unique
The value should be consistent accross all values
It can be used to set a default value for that particular class
It can be accessed by all the instance methods'''

import datetime

class Employee:
    raise_amount = 0.05 # this is the raise amount by which the pay is increased
    num_of_employees = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = f'{firstname}.{lastname}@gmail.com'.lower()

        # In this main method we can ince=rease the number of employees after every instance of the class
        Employee.num_of_employees += 1

    def show_fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    def raise_pay(self):
        new_pay = self.pay + (self.pay * self.raise_amount) # or Employee.raise_amount
        return new_pay
    

    ''''----------------   CLASS METHODS   ----------------'''

    '''They are different from instance methods. Instance methods take the self parameter.
    Class methods are associated with the class itself instead of the instances
    These methods are for the class
    to create a class method we make use of decorators
    They are like functions that take another function as an argument and returns a modified version of that function
    Decorators look like this: @classmethod
    They take "cls" as their first argument instead of self'''

    @classmethod
    def set_pay_percent(cls, amount):
        cls.raise_amount = amount
        print(f'Pay percentage has been raised to {amount}')



    ''''----------------   STATIC METHODS   ----------------'''
    '''They are not used on instances nor classes but somehow have a logical connection to the classes
    They also use decorators @staticmethod'''

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
employee1 = Employee('Rhoda', 'Oduro-Nyarko', 50000)
employee2 = Employee('Rhoda', 'Oduro-Nyarko', 50000)
print(employee1.show_fullname())
print(employee1.pay)
print(employee1.raise_pay())
print(employee1.email)
print(Employee.num_of_employees)

date_today = datetime.datetime.now()
print(Employee.is_work_day(date_today))



