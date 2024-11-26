from config import session
from models import Laptops



class LaptopsCrud:
    def __init__(self, session):
        self.session = session

    def insert_laptop(self, laptop_name, laptop_number, student_id):
        new_laptop = Laptops(laptop_name = laptop_name, laptop_number = laptop_number, student_id = student_id)
        self.session.add(new_laptop)
        self.session.commit()
        return f'Laptop with name {laptop_name} and number {laptop_number} has been assigned to student with student-id: {student_id}'
    
    def select_all_laptop(self):
        return self.session.query(Laptops).all()
    
    def select_laptop_by_laptop_name(self, laptop_name):
        return self.session.query(Laptops).filter_by(laptop_name = laptop_name).first()
    
    def select_laptop_by_number(self, laptop_number):
        return self.session.query(Laptops).filter_by(laptop_number = laptop_number).first()
    
    def select_laptop_by_student_id(self, student_id):
        return self.session.query(Laptops).filter_by(student_id = student_id).first()
    
    def update_laptop(self, laptop_number, laptop_name = None, student_id = None):
        selected_laptop = self.session.query(Laptops).filter_by(laptop_number = laptop_number).first()
        if selected_laptop:
            if laptop_name:
                selected_laptop.laptop_name = laptop_name
            if student_id:
                selected_laptop.student_id = student_id
            self.session.commit()
        return selected_laptop
    
    def delete_laptop(self, laptop_number):
        selected_laptop = self.session.query(Laptops).filter_by(laptop_number = laptop_number).first()
        if selected_laptop:
            self.session.delete(selected_laptop)
        self.session.commit()
        return f'Laptop with laptop number: {laptop_number} has been removed.'




# Creating an instance of the LaptopsCrud class for this session
laptopscrud = LaptopsCrud(session)



# Inserting new laptop data into the laptops table
new_laptop = laptopscrud.insert_laptop('Hp Pavillion', 1000, 1)
new_laptop = laptopscrud.insert_laptop('Hp Elite Book', 1001, 2)
new_laptop = laptopscrud.insert_laptop('Apple MacBook Air M2', 1002, 3)
new_laptop = laptopscrud.insert_laptop('MSI GF63 Thin', 1003, 4)
new_laptop = laptopscrud.insert_laptop('Acer Aspire 5', 1004, 5)
new_laptop = laptopscrud.insert_laptop('Lenovo IdeaPad Slim 3', 1005, 6)

'''
Output
mysql> SELECT * FROM laptops;
+-----------------------+---------------+------------+
| laptop_name           | laptop_number | student_id |
+-----------------------+---------------+------------+
| Hp Pavillion          |          1000 |          1 |
| Hp Elite Book         |          1001 |          2 |
| Apple MacBook Air M2  |          1002 |          3 |
| MSI GF63 Thin         |          1003 |          4 |
| Acer Aspire 5         |          1004 |          5 |
| Lenovo IdeaPad Slim 3 |          1005 |          6 |
+-----------------------+---------------+------------+
6 rows in set (0.00 sec)
'''



# Querying all laptops in the laptops table
all_laptops = laptopscrud.select_all_laptop()
for laptop in all_laptops:
    print(laptop)

'''Output
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ python3 laptops_crud.py
Located and connected to database
Laptop name: Hp Pavillion, Laptop number: 1000 Student id: 1
Laptop name: Hp Elite Book, Laptop number: 1001 Student id: 2
Laptop name: Apple MacBook Air M2, Laptop number: 1002 Student id: 3
Laptop name: MSI GF63 Thin, Laptop number: 1003 Student id: 4
Laptop name: Acer Aspire 5, Laptop number: 1004 Student id: 5
Laptop name: Lenovo IdeaPad Slim 3, Laptop number: 1005 Student id: 6
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ 
'''


# Select laptop based on the laptop name
laptop_by_name = laptopscrud.select_laptop_by_laptop_name('Hp Pavillion')
print(laptop_by_name)

'''Output
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ python3 laptops_crud.py
Located and connected to database
Laptop name: Hp Pavillion, Laptop number: 1000 Student id: 1
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ 
'''



# Query laptop bases on the laptop number
laptop_by_number = laptopscrud.select_laptop_by_number(1004)
print(laptop_by_number)

'''Output
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ python3 laptops_crud.py
Located and connected to database
Laptop name: Acer Aspire 5, Laptop number: 1004 Student id: 5
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ 
'''



#Select laptop based on the student id
laptop_by_student_id = laptopscrud.select_laptop_by_student_id(6)
print(laptop_by_student_id)

'''Output
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ python3 laptops_crud.py
Located and connected to database
Laptop name: Lenovo IdeaPad Slim 3, Laptop number: 1005 Student id: 6
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ 
'''



'''Updating the Database'''
laptop_to_update = laptopscrud.update_laptop(1003, laptop_name = 'Huawei MateBook X Pro')
print(laptop_to_update)

'''Output
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ python3 laptops_crud.py
Located and connected to database
Laptop name: Huawei MateBook X Pro, Laptop number: 1003 Student id: 4
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ 
'''



'''Deleting a record from our table'''
laptop_to_delete = laptopscrud.delete_laptop(1005)
print(laptop_to_delete)

'''Output
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ python3 laptops_crud.py
Located and connected to database
Laptop with laptop number: 1005 has been removed.
(myenv) rhodalee@Rhoda-Lee:~/HACSA_LESSONS/Databases/sql_alchemy$ 
'''



# I select all laptops in MySQL to see if record was deleted
'''Output
mysql> SELECT * FROM laptops;
+-----------------------+---------------+------------+
| laptop_name           | laptop_number | student_id |
+-----------------------+---------------+------------+
| Hp Pavillion          |          1000 |          1 |
| Hp Elite Book         |          1001 |          2 |
| Apple MacBook Air M2  |          1002 |          3 |
| Huawei MateBook X Pro |          1003 |          4 |
| Acer Aspire 5         |          1004 |          5 |
+-----------------------+---------------+------------+
5 rows in set (0.01 sec)
'''

