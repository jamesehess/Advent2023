# -----------------------
#   Advent of Code 2023
#   Day 1 Part 1
#   Author: Aldinach
# -----------------------

import re

inputs = []
numbers = []
values = []

with open("Day1Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip())

for input in inputs:


    firstnumber = re.search('[0-9]', input).group()
    lastnumber = re.findall('[0-9]', input)

    number = firstnumber + lastnumber[-1]
    numbers.append(int(number))


print(sum(numbers))