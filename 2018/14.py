#!/bin/python3

file = open("input/14.txt", "r")


inputNumber = 0
inputLength = 0
recipes = [3, 7]
firstIdx = 0
secondIdx = 1


def parseInput():
    global inputNumber
    global inputLength
    inputNumber = int(file.readline())
    inputLength = len(str(inputNumber))
    print(inputNumber)
    print(inputLength)


def addNewRecipes():
    global recipes
    global firstIdx
    global secondIdx
    global inputLength
    global inputNumber
    newVal = recipes[firstIdx] + recipes[secondIdx]

    if newVal > 9:
        recipes.append(1)
        if checkEnd() is True:
            return True
        recipes.append(newVal - 10)
    else:
        recipes.append(newVal)

    return checkEnd()


def updateElvesPos():
    global recipes
    global firstIdx
    global secondIdx
    firstIdx = firstIdx + recipes[firstIdx] + 1
    secondIdx = secondIdx + recipes[secondIdx] + 1

    if firstIdx >= len(recipes):
        firstIdx = firstIdx  % len(recipes)

    if secondIdx >= len(recipes):
        secondIdx = secondIdx  % len(recipes)


def checkEnd():
    global recipes
    global inputLength
    if len(recipes) < inputLength:
        return False

    for i, val in enumerate(recipes[-inputLength::]):
        if val != int(str(inputNumber)[i]):
            return False

    return True


def main():
    global inputNumber
    parseInput()

    while True:
        if addNewRecipes() is True:
            break
        updateElvesPos()
        print(len(recipes))

    print("MATCH")
    print(len(recipes) - inputLength)


if __name__ == '__main__':
    main()
