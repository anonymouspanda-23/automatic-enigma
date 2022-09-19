# Name:
# Email ID:
import re

def get_sum_of_digits(my_str) -> int:
    matches = re.findall("[0-9]", my_str)
    if not matches:
        return 0
    
    sum = 0
    
    for number in matches:
        sum += int(number)
    
    return sum