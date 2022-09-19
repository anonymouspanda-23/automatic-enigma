# Name:
# Email ID:

import re

def check_math(list_of_equations):
    num_eqn = len(list_of_equations)

    if num_eqn == 0:
        return True
    
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y
    }

    valid_eqns = True
    
    for eqn in list_of_equations:
        eqn = eqn.replace(' ', '')
        numbers = re.findall("[0-9]{0,}", eqn)
        
        while '' in numbers:
            numbers.remove('')
        
        for idx, num in enumerate(numbers):
            numbers[idx] = int(num)
        operator = re.findall("\+|\-|\*|\/\/|\%", eqn)[0]
        
        result = operators[operator](numbers[0], numbers[1])
        if not result == numbers[2]:
            valid_eqns = False
            break
    
    return valid_eqns
