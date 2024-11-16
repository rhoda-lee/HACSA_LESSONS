from inheritance import Employee


class Software_Engineer(Employee):
    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang

swe1 = Software_Engineer('Rhoda', 'Dede', 98000, 'Python')

swe2 = Software_Engineer('Dede', 'Oduro-Nyarko', 98000, 'Java')
print(swe1.prog_lang)



class Project_Manager(Employee):
    def __init__(self, firstname, lastname, pay, department, employees = None):
        super().__init__(firstname, lastname, pay)
        self.department = department
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        '''Add an employee to Managers list of employees'''
        if emp not in self.employees:
            self.employees.append(emp)
        return f'Employee:- {emp.show_fullname()} has been added to the manager\'s employees\n'
    
    def show_all_employees(self):
        """Showing all employees"""
        for emp in self.employees:
            print(f'Manager is Managing these employees\n{emp.show_fullname()}\n')

    def remove_employee(self, emp):
        '''Removing an employee'''
        if emp in self.employees:
            self.employees.remove(emp)
        return f'Employee {emp.show_fullname()} has been removed from the manager\'s list\n'
    
    def __repr__(self):
        '''official Prepresentation'''
        return f'\n{self.firstname} {self.lastname} {self.pay} {self.department}\n'
    
    def __str__(self):
        '''Unofficial Representation'''
        return f'\n{self.firstname} {self.lastname} earns {self.pay} and belongs to {self.department} department\n'


manager1 = Project_Manager('Rhoda', 'Lee', 98000, 'Marketing', [swe1])

print(manager1)

print(manager1.show_fullname())
print(manager1.add_employee(swe2))
manager1.show_all_employees()

print(manager1.remove_employee(swe2))
manager1.show_all_employees()



'''----------------  MAGIC / DUNDER METHODS  -------------------'''
'''These are special methods in python that have double underscores before and after them
They describe how particular methods should behave
Used to change or define how a method should behave inside a class'''

'''The __repr__ representation is the official representation of an object.
It is best to create in such a way that it tells a developer how to create a specific method
It is advicable to use f-strings
refer to Manager class


The __str__ representation is the opposite of the __repr__ representation.
It is a nice and informal representation of objects meant for user intead of developers
__str__ overridesthe __repr__
refer to Manager class'''

'''Uses of double and single underscores
Getters,  setters or property decorators'''