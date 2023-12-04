# -----------------------
#   Advent of Code 2023
#   Day 1 Part 1
#   Author: Aldinach
# -----------------------

import re

inputs = []
numbers = []
values = []

with open("Day1\Day1Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip())

for input in inputs:


    firstnumber = re.search('[0-9]|one|two|three|four|five|six|seven|eight|nine', input).group()
    lastnumber = re.findall('[0-9]|one|two|three|four|five|six|seven|eight|nine', input)

    number = firstnumber + lastnumber[-1]
    number = number.replace("one", "1")
    number = number.replace("two", "2")
    number = number.replace("three", "3")
    number = number.replace("four", "4")
    number = number.replace("five", "5")
    number = number.replace("six", "6")
    number = number.replace("seven", "7")
    number = number.replace("eight", "8")
    number = number.replace("nine", "9")

    numbers.append(int(number))


print(sum(numbers))