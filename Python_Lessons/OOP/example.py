# classes
# objects
# methods

class Animals:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.weight = 30
        

    def eat(self):
        return f'{self.name} is eating!'
    
    def sleep(self):
        return f'{self.name} is sleeping!'
    
    def walk(self):
        return f'{self.name} is walking!'
    
dog = Animals('Bob', 'Black', 2)
cat = Animals('Gigi', 'Ginger', 8)

print(f'The cat called {cat.name} is {cat.age} years old\n')

print(dog.eat())
print(dog.walk())

print(cat.weight)


'''Make a class called restaurant
The __init__ method for restaurant should store two attributes, a restaurant name and a cuisine type
Make a method called describe restaurant that prints two pieces of information
And another method called open restaurant that prints a message
indicating that the restaurant is open
Make two instances from your restaurant class
Print two attributes individually and then call both methods'''

'''MAGIC METHODS/DUNDER METHODS
__init__, __str__, __repr__, __tablename__'''




class Car:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0
    
    def start(self):
        return f'The car has started.....vrooom!!!!'
    
    def details(self):
        return f'{self.model} {self.make} {self.year}'
    
    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            return f'The new odometer reading is {mileage}'
        else:
            return f'You cannot roll back an odometer!'
    
    def increase_odometer(self, mileage):
        distance = self.odometer_reading + mileage
        return f'The new odometer reading is {distance} miles\n'
    

car1 = Car('Toyota', 'Camry', 2020)
print(f'Odometer reading is {car1.odometer_reading}\n')

print(car1.odometer_reading)
print(car1.update_odometer_reading(500))
print(car1.update_odometer_reading(500))
print(car1.odometer_reading)
print(car1.update_odometer_reading(50))
print(car1.increase_odometer(50))


# new_odometer_reading = car1.odometer_reading + 23
# print(new_odometer_reading)


'''--------------INHERITANCE--------------
child class (sub class): inherits from some class
parent class (super class): passes it's features to another class'''

class Employee:
    rate = 0.05
    number_of_employees = 0

    def __init__(self, fullname, pay):
        self.fullname = fullname
        self.pay = pay
        self.email = f'{fullname}.dev@gmail.com'.lower().replace(' ', '')
        Employee.number_of_employees += 1


    def show_fullname(self):
        return f'Name of employee is: {self.fullname}'
    
    def raise_pay(self):
        new_pay = self.pay + (self.pay * self.rate)
        return new_pay
    
    @classmethod
    def new_rate(cls, new_percentage_rate):
        cls.rate = new_percentage_rate
        return f'The pay increase rate has been updated to {new_percentage_rate}'
    
    def __str__(self):
        return f'Employee by name {self.fullname} and email {self.email} earns {self.pay}'
    
print(Employee.new_rate(0.5))
# emp1 = Employee('Rhoda Lee', 4000)
# emp2 = Employee('Beatrice Appiah', 6000)
# print(emp1)

class SoftwareEngineer(Employee):
    def __init__(self,fullname, pay, department):
        super().__init__(fullname, pay)
        self.department = department

swe1 = SoftwareEngineer('Anna Mercy', 5000, 'Marketing')
print(swe1.show_fullname())



    