#!/bin/python3

file = open("input/14.txt", "r")


inputNumber = 0
recipes = [3, 7]
firstIdx = 0
secondIdx = 1


def parseInput():
    global inputNumber
    inputNumber = int(file.readline())
    print(inputNumber)


def addNewRecipes():
    global recipes
    global firstIdx
    global secondIdx
    newVal = recipes[firstIdx] + recipes[secondIdx]

    if newVal > 9:
        recipes.append(1)
        recipes.append(newVal - 10)
    else:
        recipes.append(newVal)

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


def main():
    global inputNumber
    parseInput()
    while len(recipes) < (inputNumber + 10):
        addNewRecipes()
        updateElvesPos()
    print(len(recipes))
    print(recipes)
    for i in recipes[-10::]:
        print(i, end="")
    print("")


if __name__ == '__main__':
    main()
