#!/bin/python3

file = open("input/12.txt", "r")

pots = []
nextPots = []
rules = []
idxOffset = 0


def initialState(line):
    global pots
    global idxOffset
    state = line.split(": ")[1]
    print(state)
    for char in state:
        if char == '.':
            pots.append(False)
        elif char == '#':
            pots.append(True)
    pots = [False] * 30 + pots + [False] * 200
    idxOffset = -30


def printState(array):
    for val in array:
        if val is True:
            print("#", end="")
        else:
            print(".", end="")
    print("")


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


def checkEnd():
    global pots
    global nextPots
    printState(pots[0:-1])
    printState(nextPots[1::])
    return pots[0:-1] == nextPots[1::]


def applyRules():
    global pots
    global rules
    global nextPots
    nextPots = pots.copy()
    for i in range(len(pots[2:-3])):
        for rule in rules:
            if rule[0] == pots[i-2:i+3]:
                nextPots[i] = rule[1]
    ret = checkEnd()
    pots = nextPots
    printState(pots)
    return ret


def main():
    parseInput()
    i = 0
    while applyRules() is False:
        i = i + 1
    print(i)

    total = 0
    nb = 0
    for j, val in enumerate(pots):
        if val is True:
            total = total + j + idxOffset + 50000000000 - i - 1
    print(total)


if __name__ == '__main__':
    main()
