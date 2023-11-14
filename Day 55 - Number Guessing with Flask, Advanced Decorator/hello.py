from flask import Flask

app = Flask(__name__)

# custom decorator
# making bold text
def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

# making emphasis (italic)
def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>\
        <p>This is a paragraph</p>\
        <img src="https://media.giphy.com/media/K1tgb1IUeBOgw/giphy.gif" width=400 />'
        

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


# Creating variable paths and converting the path to a specific data type
@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

# __name__ is the special attribute in python it is the class, function name
if __name__ == "__main__":
    app.run(debug=True)