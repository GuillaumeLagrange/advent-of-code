#!/bin/python3

file = open("input/12.txt", "r")

pots = []
rules = []
idxOffset = 0


def initialState(line):
    state = line.split(": ")[1]
    print(state)
    for char in state:
        if char == '.':
            pots.append(False)
        elif char == '#':
            pots.append(True)


def rule(line):
    [ruleStr, resultStr] = line.split(" => ")
    if len(ruleStr) != 5:
        print("Error")
    ruleArray = []
    result = False
    for char in ruleStr:
        if char == '.':
            ruleArray.append(False)
        elif char == '#':
            ruleArray.append(True)

    if resultStr[0] == '.':
        result = False
    elif resultStr[0] == '#':
        result = True

    rules.append((ruleArray, result))


def parseInput():
    line = file.readline()
    initialState(line)
    file.readline()  # Blank line
    for line in file:
        rule(line)


def applyRule(rule, index):


def main():
    parseInput()


if __name__ == '__main__':
    main()
