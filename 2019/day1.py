#!/bin/python3

file = open("input/day1.txt", "r")

def parseInput():
    result = 0
    fuel = 0

    for line in file:
        fuel = ((int(line) / 3) - 2)
        while fuel > 0:
            result = result + fuel
            fuel = fuel / 3 - 2

    print(result)


def main():
    parseInput()


if __name__ == '__main__':
    main()
