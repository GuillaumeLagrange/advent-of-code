#!/bin/python3

file = open("input/1.txt", "r")


def parseInput():
    shifts = []
    values = {0}
    ret = 0
    for line in file:
        ret += int(line.strip())
        shifts.append(int(line.strip()))
        if ret in values:
            print(ret)
            return
        values.add(ret)

    while True:
        for shift in shifts:
            ret += shift
            if ret in values:
                print(ret)
                return
            values.add(ret)



def main():
    parseInput()


if __name__ == '__main__':
    main()
