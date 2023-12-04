# -----------------------
#   Advent of Code 2023
#   Day 2 Part 1
#   Author: James Hess
# -----------------------

import re

inputs = []
gameIDs = []

with open("Day2Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip())

for input in inputs:
    # For each game, get the game number and store the cube counts in a list of lists
    cubes = []
    input = input.split(":")
    gameID = input[0].split(" ")[-1]
    cubeinput = re.split(';|,', input[1])
    for cube in cubeinput:
        cubes.append(cube.strip().split(" "))

    # Determine if game is valid if only 12 red cubes, 13 green cubes, and 14 blue cubes
    validRed = 12
    validGreen = 13
    validBlue = 14
    valid = True
    for pull in cubes:
        if pull[1] == "red":
            if int(pull[0]) > validRed:
                valid = False
        elif pull[1] == "green":
            if int(pull[0]) > validGreen:
                valid = False
        elif pull[1] == "blue":
            if int(pull[0]) > validBlue:
                valid = False

    # If valid, then store game id
    if valid is True:
        gameIDs.append(int(gameID))


print(sum(gameIDs))