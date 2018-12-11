#!/bin/python3

file = open("input/11.txt", "r")

serialNumber = 0
fuelGrid = [[0] * 300 for i in range(300)]
squares = [[0] * 297 for i in range(297)]

def parseInput():
    global serialNumber
    serialNumber = int(file.readline())


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


def generateFuelGrid():
    global fuelGrid
    for i in range(300):
        for j in range(300):
            fuelGrid[i][j] = calcPowerLevel(i+1, j+1) # x and y start at 1

def calcSquarePowerLevel(x, y):
    global fuelGrid
    squarePowerLevel = 0
    for i in range(3):
        for j in range(3):
            squarePowerLevel = squarePowerLevel + fuelGrid[x + i][y +j]
    return squarePowerLevel

def generateSquares():
    global squares
    for i in range(297):
        for j in range(297):
            squares[i][j] = calcSquarePowerLevel(i, j)

def findMaxSquare():
    global squares
    maxVal = 0
    maxX = 0
    maxY = 0
    for i in range(297):
        for j in range(297):
            if squares[i][j] > maxVal:
                maxVal = squares[i][j]
                maxX = i + 1
                maxY = j + 1
    return maxX, maxY

def main():
    parseInput()
    generateFuelGrid()
    generateSquares()
    x, y = findMaxSquare()
    print("X %d, Y %d" % (x, y))


if __name__ == '__main__':
    main()
