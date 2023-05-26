#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == 'admin' and password == '12345':
        return 'Access granted'
    
    return 'Access denied'

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature <65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    
    return "It's perfect out there!"

def fizzbuzz(num):
    if (num % 3) == 0:
        if (num % 5) == 0:
            return 'FizzBuzz'
        
        return 'Fizz'
    elif (num % 5) == 0:
        return 'Buzz'
    
    return num

def calculator(operation, num1, num2):
    if operation in ('+', '-', '*', '/'):
        try:
            result = eval(f"{num1} {operation} {num2}")
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
    else:
        print('Invalid operation!')
        return None

# def calculator(operation, num1, num2):
#     if operation in ('+', '-', '*', '/'):
#         return eval(f'{num1} {operation} {num2}')
#     else:
#         return 'Invalid operation!'
    

    # if operation == '+' or operation == '-' or operation == '*' or operation == '/':
    #     return (num1 + operation + num2)
    # else:
    #     return 'Invalid operation!'
