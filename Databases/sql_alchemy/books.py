from flask import Blueprint, jsonify, request

books_bp = Blueprint('books', __name__)



# defining a list of dicitonaries
books = [
    {'id':1,
     'title':'1984',
     'author':'George Orwell'
    },

    {'id':2,
     'title':'To Kill a Mocking Bird',
     'author':'Harper Lee'
    },

    {'id':3,
     'title':'YOU',
     'author':'Caroline kepnes'
    },
]


# books endpoint, specify methods to use
@books_bp.route('/books', methods = ['GET'])
def get_all_books():
    # function to make sure our response always comes in a JSON file
    return jsonify(books), 200


# endpoint to get a specific book
@books_bp.route('/books/<int:book_id>', methods = ['GET'])
def get_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book), 200
       
    return jsonify({'error':'Book not found'}), 404


# endpoint to get book based on author
@books_bp.route('/books/<string:author_name>', methods = ['GET'])
def get_book_by_author(author_name):
    for book in books:
        if book['author'] == author_name:
            return jsonify(book), 200
        
    return jsonify({'error': 'Author not found'}), 404


# Making Post Requests, use request function, needs to be imported to get the body of a request
@books_bp.route('/books', methods = ['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'New Book': new_book})


# Update an already existing book, update a specific book, so we use PATCH request
@books_bp.route('/books/<int:book_id>', methods = ['PATCH'])
def update_book_by_id(book_id):
    data_to_update = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book.update(data_to_update)
            return jsonify(book), 200
    return jsonify({'Error':'Book not found'}), 404


# API endpoint to update a book based on it's title
@books_bp.route('/books/<string:book_title>', methods = ['PATCH'])
def update_book_by_title(book_title):
    book_to_update = request.get_json()
    for book in books:
        if book['title'] == book_title:
            book.update(book_to_update)
            return jsonify(book), 200
        
    return jsonify({'Error': 'Book Not Found!'}), 404


@books_bp.route('/books/<int:book_id>', methods = ['DELETE'])
def delete_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'Message': f'Book with ID: {book_id} has been deleted!'}), 200
        
    return jsonify({'Error': 'Book not Found'}), 404