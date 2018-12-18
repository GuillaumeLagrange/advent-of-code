#!/bin/python3

file = open("input/18.txt", "r")

area = []
same = False


def printArea():
    global area
    for line in area:
        print("".join(line))
    print("")


def parseInput():
    global area
    for line in file:
        array = []
        for char in line.strip():
            array.append(char)
        area.append(array)
    printArea()


def step():
    global area
    global same
    nArea = [line.copy() for line in area]
    for i, line in enumerate(area):
        for j, val in enumerate(line):
            neighbours = {"#" : 0, "|" : 0, "." : 0}
            # Find neighbours
            if i > 0:
                for nVal in area[i - 1][max(0, j - 1):min(len(line), j + 2)]:
                    neighbours[nVal] = neighbours[nVal] + 1
            if i < len(area) - 1:
                for nVal in area[i + 1][max(0, j - 1):min(len(line), j + 2)]:
                    neighbours[nVal] = neighbours[nVal] + 1
            if j > 0:
                neighbours[line[j - 1]] = neighbours[line[j - 1]] + 1
            if j < len(line) - 1:
                neighbours[line[j + 1]] = neighbours[line[j + 1]] + 1

            # Evolve
            if val == ".":
                if neighbours["|"] >= 3:
                    nArea[i][j] = "|"
                else:
                    nArea[i][j] = "."
            elif val == "|":
                if neighbours["#"] >= 3:
                    nArea[i][j] = "#"
                else:
                    nArea[i][j] = '|'
            elif val == "#":
                if (neighbours["#"] >= 1) and (neighbours["|"] >= 1):
                    nArea[i][j] = "#"
                else:
                    nArea[i][j] = "."

    if area == nArea:
        same = True

    area = nArea


def main():
    global same
    areas = []
    parseInput()
    for i in range(600):
        step()
        printArea()

    cycle = 0
    for i in range(100):
        if area in areas:
            print("Cycle !", i)
            cycle = i
            break
        areas.append([line.copy() for line in area])
        step()

    futureArea = areas[(1000000000 - 600) % cycle]

    nTree = 0
    nLumb = 0
    for line in futureArea:
        for val in line:
            if val == "#":
                nLumb = nLumb + 1
            elif val == "|":
                nTree = nTree + 1

    print(same)
    print(nTree * nLumb)


if __name__ == '__main__':
    main()
