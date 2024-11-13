
''''----------------   INHERITANCE   ----------------'''

'''This is when a class inherits from another class.
We do this when we want to create a class that is similar to an already existing class
The already existing class is called the parent class and the one inheriting is the child class
The child class can access any or all of the attributes and methods of the child class'''




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





# This class inherits fro the employee class

class Software_Engineer(Employee):
    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang






swe1 = Software_Engineer('Rhoda', 'Lee', 92000, 'Python')
print(swe1.show_fullname())
print(swe1.prog_lang)


swe2 = Software_Engineer('Rhoda', 'Oduro-Nyarko', 87000, 'JavaScript')
print(swe2.show_fullname())
print(swe2.prog_lang)




class Project_Manager(Employee):
    def __init__(self, firstname, lastname, pay, department):
        super().__init__(firstname, lastname, pay)
        self.department = department

pm1 = Project_Manager('Habiba', 'Adam Salisu', 92000, 'IT Department')
print(pm1.show_fullname())
print(pm1.department)

