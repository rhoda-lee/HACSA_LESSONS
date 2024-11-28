from flask import Flask, jsonify, request

app = Flask(__name__)

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

# Creating an endpoint with Flask use @route decorator: @app.route('/') where '/' is the home directory
@app.route('/')
def home():
    return 'Welcome to Flask'

# Endpoint 2
@app.route('/another_home')
def another_home():
    return 'This is just another Home'

# books endpoint, specify methods to use
@app.route('/books', methods = ['GET'])
def get_all_books():
    # function to make sure our response always comes in a JSON file
    return jsonify(books), 200

# endpoint to get a specific book
@app.route('/books/<int:book_id>', methods = ['GET'])
def get_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book), 200
       
    return jsonify({'error':'Book not found'}), 404

# endpoint to get book based on author
@app.route('/books/<string:author_name>', methods = ['GET'])
def get_book_by_author(author_name):
    for book in books:
        if book['author'] == author_name:
            return jsonify(book), 200
        
    return jsonify({'error': 'Author not found'}), 404


# Making Post Requests, use request function, needs to be imported to get the body of a request
@app.route('/books', methods = ['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'New Book': new_book})

# Have backend server run
if __name__ == '__main__':
    app.run(debug=True)



# Write api endpoint that gets a book based on Author