# -----------------------
#   Advent of Code 2023
#   Day 3 Part 1
#   Author: James Hess
# -----------------------

import re

lines = []
valids = []
total = 0

with open("Day3Input.txt") as file:
    inputlines = file.readlines()
    for inputline in inputlines:
        lines.append(inputline.strip())

for y in range(len(lines)):
    numbers = re.findall('\d+', lines[y])
    for number in numbers:
        valid = False
        numberStart = re.search(number, lines[y]).start()
        numberLength = len(re.search(number, lines[y]).group())
        # Look Before for symbol
        if numberStart != 0:
            print("Searching Before " + str(number) + ": Y=" + str(y) + " X=" + str(numberStart - 1) + " Valid=" + str(valid) + " Char=" + str(lines[y][numberStart-1]))
            if re.search('[.]|[0-9]', lines[y][numberStart-1]) is None:
                valid = True
        # Look After for symbol
        if numberStart+numberLength < 140:
            print("Searching After " + str(number) + ": Y=" + str(y) + " X=" + str(numberStart+numberLength) + " Valid=" + str(valid) + " Char=" + str(lines[y][numberStart+numberLength]))
            if re.search('[.]|[0-9]', lines[y][numberStart+numberLength]) is None:
                valid = True
        # Look Above for symbol
        if y-1 >= 0:
            for x in range(numberStart-1,numberStart+numberLength+1):
                if x >= 0 and x < 140: # Make sure we are in range
                    print("Searching Above " + str(number) + ": Y=" + str(y - 1) + " X=" + str(x) + " Valid=" + str(valid) + " Char=" + str(lines[y-1][x]))
                    if re.search('[.]|[0-9]', lines[y-1][x]) is None:
                        valid = True
        # Look Below for symbol
        if y+1 < 140:
            for x in range(numberStart-1, numberStart+numberLength+1):
                if x >= 0 and x < 140: # Make sure we are in range
                    print("Searching Below " + str(number) + ": Y=" + str(y + 1) + " X=" + str(x) + " Valid=" + str(valid) + " Char=" + str(lines[y+1][x]))
                    if re.search('[.]|[0-9]', lines[y+1][x]) is None:
                        valid = True
        # If valid then add to total
        if valid is True:
            valids.append(int(number))


print(sum(valids))
