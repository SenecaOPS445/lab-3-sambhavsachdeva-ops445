#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: ssachdeva25

def operate(number1, number2, operator):
    # Check the operator and perform the corresponding operation
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))         # Expected: 15
    print(operate(10, 5, 'subtract'))    # Expected: 5
    print(operate(10, 5, 'multiply'))    # Expected: 50
    print(operate(10, 5, 'divide'))      # Expected: Error message
