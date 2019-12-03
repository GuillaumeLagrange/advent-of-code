#!/bin/python3

file = open("input/day2.txt", "r")

mem = []
index = 0

def parseInput():
    global mem
    for line in file:
        mem = [int(i) for i in line.strip().split(',')]
    mem[1] = 12
    mem[2] = 2

def executeStep():
    global mem
    global index
    [opcode, op1, op2, op3] = mem[index:(index + 4)]

    if opcode == 1:
        mem[op3] = mem[op1] + mem[op2]
    elif opcode == 2:
        mem[op3] = mem[op1] * mem[op2]
    else:
        return False

    index = index + 4

    return True


def main():
    global mem
    parseInput()

    print mem

    while executeStep():
        pass

    print mem


if __name__ == '__main__':
    main()
