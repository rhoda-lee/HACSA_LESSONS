from flask import Flask, jsonify, request
from backend_crud import BackendCrud
from config import session
from books import books_bp

app = Flask(__name__)
backend_crud = BackendCrud(session)
app.register_blueprint(books_bp)


# Creating an endpoint with Flask use @route decorator: @app.route('/') where '/' is the home directory
@app.route('/')
def home():
    return 'Welcome to Flask'


@app.route('/students', methods = ['GET'])
def get_all_students():
    students = backend_crud.get_all_students()
    students_list = []
    for student in students:
        students_list.append({
            'id': student.student_id,
            'firstname': student.first_name,
            'lastname': student.last_name,
            'email': student.email
        })
    return jsonify(students_list)


@app.route('/students/<string:first_name>', methods = ['GET'])
def get_by_firstname(first_name):
    student = backend_crud.get_student_by_first_name(first_name)
    return jsonify({
        'id': student.student_id,
        'firstname': student.first_name,
        'lastname': student.last_name,
        'email': student.email
    })


# POST request
@app.route('/students', methods = ['POST'])
def add_student():
    details = request.get_json()
    if details is not None:
        new_student = backend_crud.insert_student(
            first_name = details.get('first_name'),
            last_name = details.get('last_name'),
            email = details.get('email'),
            age = details.get('age')
        )
        return jsonify({'New Student Added': {
            'id': new_student.student_id,
            'first_name': new_student.first_name,
            'last_name': new_student.last_name,
            'email': new_student.email
        }})
    else:
        return jsonify({'Error': 'Bad request'}), 400



# Have backend server run
if __name__ == '__main__':
    app.run(debug=True)



# Write api endpoint that gets a book based on Author