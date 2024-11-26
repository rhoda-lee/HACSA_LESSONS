from config import session
# used to create a base class or parent for all models They'll all inherit from declarative base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Backend(Base):
    __tablename__ = 'backend_class'
    student_id = Column(Integer, primary_key = True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    age = Column(Integer, nullable = False)
    email = Column(String(100), nullable = False, unique = True)

    laptops = relationship('Laptops', back_populates = 'student')

    def __str__(self):
        return f"Student's ID: {self.student_id}, Name: {self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}"


class Laptops(Base):
    __tablename__ = 'laptops'
    laptop_name = Column(String(100), nullable = False, unique = True)
    laptop_number = Column(Integer, primary_key = True, nullable = False)
    student_id = Column(Integer, ForeignKey('backend_class'))

    student = relationship('Backend', back_populates = 'laptops')

    def __str__(self):
        return f'Laptop name: {self.laptop_name}, Laptop number: {self.laptop_number} Student id: {self.student_id}'


# Create laptops_crud.py to apply crud operations

# session.bind ensures the table is created in the same database we are connected to
if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Tables created successfully!')
    except Exception as e:
        print(f'An error occured: {e}')
    # The code above creates the tables

    


'''session.add() is used to add new record to the database
After adding, changinges are pending like git add
Hence after session.add() we use 

session.commit()
It is used to save changes to the database

session.query().all retrieves all data from a table in a database, like SELECT * FROM table_name

session.filter_by() Used to get a specific data based on a condition or criteria

session.delete() used to delete a record'''

