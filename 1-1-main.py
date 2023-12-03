import os
import re

filename = '1-1-data.txt'

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

def extract_numbers(filename):
    sum = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        numbers_in_line = (str("".join(re.findall(r"\d+", line))))
        numbers = int(numbers_in_line[0] + numbers_in_line[-1])
        sum += numbers
    
    print(sum)

extract_numbers(filename)