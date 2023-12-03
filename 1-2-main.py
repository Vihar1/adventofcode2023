import os
import re

filename = '1-1-data.txt'
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def extract_numbers(filename):
    sum = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        for key in numbers:
            print(line.replace(key, str(numbers[key])))
"""   for replaced in lines:
        for key in numbers:
            replaced = replaced.replace(key, str(numbers[key])) """
        
"""     numbers_in_line = (str("".join(re.findall(r"\d+", replaced))))
    numbers_digits = int(numbers_in_line[0] + numbers_in_line[-1])
    print(f"{replaced} - {numbers_digits}")
    sum += numbers_digits
     """
    print(sum)

extract_numbers(filename)