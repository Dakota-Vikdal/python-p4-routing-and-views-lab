#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


# @app.route('/<string:username>')
# def user(username):
    # return f'<h1>Profile for {username}</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    return f'<h1>{parameter}</h1><br/>'

@app.route("/count/<int:numgiven>")
def count(numgiven:int):
    the_string = ""
    for n in range(numgiven):
        the_string += f"{n}<br/>"
    return the_string

@app.route("/math/<int:num1><operation><int:num2>")
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    else:
        return f'{num1 % num2}'
    




if __name__ == '__main__':
    app.run(port=5555, debug=True)
