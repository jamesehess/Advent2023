# -----------------------
#   Advent of Code 2023
#   Day 2 Part 2
#   Author: Aldinach
# -----------------------

import re

inputs = []
totalPower = 0

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

    # Determine the max cube count for each color
    redPower = 0
    greenPower = 0
    bluePower = 0
    for cube in cubes:
        if cube[1] == "red":
            if int(cube[0]) > redPower:
                redPower = int(cube[0])
        if cube[1] == "green":
            if int(cube[0]) > greenPower:
                greenPower = int(cube[0])
        if cube[1] == "blue":
            if int(cube[0]) > bluePower:
                bluePower = int(cube[0])

    # Calculate the power and add up
    gamePower = redPower * greenPower * bluePower

    totalPower = totalPower + gamePower

print(totalPower)