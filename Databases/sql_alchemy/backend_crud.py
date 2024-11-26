from config import session
from models import Backend

# Create a class that has all operations (CRUD) we can perform on the table
class BackendCrud:
    def __init__(self, session):
       self.session = session

    def insert_student(self, first_name, last_name, age, email):
        new_student = Backend(first_name = first_name, last_name = last_name, age = age, email = email)
        self.session.add(new_student)
        self.session.commit()
        return f'New student with these details {new_student} was added!'
    
    def get_all_students(self):
        return self.session.query(Backend).all()
    
    def get_student_by_first_name(self, first_name):
        return self.session.query(Backend).filter_by(first_name=first_name).first()
    
    def get_student_by_last_name(self, last_name):
        return self.session.query(Backend).filter_by(last_name=last_name).first()
    
    def update_student(self, student_id, first_name = None, last_name = None, age = None, email = None):
        selected_student = self.session.query(Backend).filter_by(student_id = student_id).first()
        if selected_student:
            if first_name:
                selected_student.first_name = first_name
            if last_name:
                selected_student.last_name = last_name
            if age:
                selected_student.age = age
            if email:
                selected_student.email = email
            self.session.commit()
        return selected_student
    
    def delete_student(self, student_id):
        selected_student = self.session.query(Backend).filter_by(student_id = student_id).first()
        if selected_student:
            self.session.delete(selected_student)
        self.session.commit()
        return f'Student with student id {student_id} has been deleted!'
    
# Creating an instance of the BackendCrud class
backend_crud = BackendCrud(session)

# Inserting new Students into the backend_class Table
new_student = backend_crud.insert_student('Rhoda', 'Lee', 22, 'rhodalee.dev@gmail.com')
new_student = backend_crud.insert_student('Nana Afua Antwiwaa', 'Conduah', 19, 'anaconduah@gmail.com')
new_student = backend_crud.insert_student('Augustine', 'Ninyung', 22, 'aninyung@gmail.com')
new_student = backend_crud.insert_student('Samuel', 'Gyasi', 23, 'sgyasi@gmail.com')
new_student = backend_crud.insert_student('Matilda', 'Baffah', 21, 'mbaffah@gmail.com')
new_student = backend_crud.insert_student('Mandy', 'Serwaa', 19, 'mserwaa@gmail.com')


#print(new_students)

# all_students = backend_crud.get_all_students()
# for student in all_students:
#     print(student)

# student_by_last_name = backend_crud.get_student_by_last_name('Lee')
# print(student_by_last_name)


# Updating data in the Backend table using an instance of the BackendCrud class
# updated_student = backend_crud.update_student(1, last_name = 'Oduro-Nyarko')
# print(updated_student)

# deleted_student = backend_crud.delete_student(5)
# print(deleted_student)

