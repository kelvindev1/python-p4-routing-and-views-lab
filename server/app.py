#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:integer>')
def count(integer):
    count = f""
    for i in range(integer):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def operations(num1, operation, num2):
    result = 0

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1/num2
        else:
            return "Invalid operation. Division by zero"
    elif operation == '%':
        result = num1 % num2
        
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

# print_string("Kelvin")