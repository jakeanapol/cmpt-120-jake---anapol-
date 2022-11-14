# The Flask package we need in order to run our REST APIs
from flask import Flask, jsonify

# Creating a new "app" by using the Flask object constructor method.
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


# Checks to see of then
if __name__ == "__main__":
    # Runs the Flask application only if this file itself being run.
    app.run()
    # Creating a "books" JSON / dict to emulate data coming from a database.
books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298"
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    }
]
@app.route("/books", methods=["GET"])
def get_books():
    # Returns the books list in JSON which stands for JavaScript Object Notation.
    return jsonify({"books": books})