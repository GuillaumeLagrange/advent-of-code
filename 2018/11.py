#!/bin/python3

file = open("input/11.txt", "r")

serialNumber = 0
squaresArray = []

def parseInput():
    global serialNumber
    serialNumber = int(file.readline())

def initSquaresArray():
    global squaresArray
    for size in range(300):
        squaresArray.append([[0] * (300 - size) for i in range(300 - size)])
        print(size)
        print(len(squaresArray[-1]))

def calcPowerLevel(x, y):
    global serialNumber
    rackId = x + 10
    powerLevel = rackId * y
    powerLevel = powerLevel + serialNumber
    powerLevel = powerLevel * rackId
    if powerLevel > 100:
        powerStr = str(powerLevel)
        powerLevel = int(powerStr[-3])
    else:
        powerLevel = 0
    powerLevel = powerLevel - 5

    return powerLevel


def calcSquarePowerLevel(x, y, size):
    global globalSquaresArray
    squarePowerLevel = 0

    if size == 1: # Generate fuel grid
        squarePowerLevel = calcPowerLevel(x + 1, y + 1) # x and y start at 1
    else:
        fuelPower = squaresArray[0]
        squarePowerLevel = squaresArray[size - 2][x][y]
        for i in range(size):
            squarePowerLevel = squarePowerLevel + fuelPower[x + i][y + size - 1]
        for j in range(size - 1):
            squarePowerLevel = squarePowerLevel + fuelPower[x + size - 1][y + j]

    return squarePowerLevel


def generateSquares():
    global squaresArray

    for size, squares in enumerate(squaresArray):
        print(size)
        for i in range(300 - size):
            for j in range(300 - size):
                squares[i][j] = calcSquarePowerLevel(i, j, size + 1)




def findMaxSquare():
    global squaresArray
    maxVal = 0
    maxX = 0
    maxY = 0
    maxSize = 0
    for size, squares in enumerate(squaresArray):
        for i in range(300 - size):
            for j in range(300 - size):
                if squares[i][j] > maxVal:
                    maxVal = squares[i][j]
                    maxX = i + 1
                    maxY = j + 1
                    maxSize = size + 1
    return maxX, maxY, maxSize



def main():
    parseInput()
    initSquaresArray()
    generateSquares()
    x, y, size = findMaxSquare()

    print("X %d Y %d size %d" %(x, y, size))


if __name__ == '__main__':
    main()
