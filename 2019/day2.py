#!/bin/python3.6

import copy

file = open("input/day2.txt", "r")

input_mem = []
mem = []
index = 0

def parseInput():
    global input_mem
    for line in file:
        input_mem = [int(i) for i in line.strip().split(',')]

def initMem(n, v):
    global mem
    global input_mem
    global index
    mem = list(input_mem)
    index = 0
    mem[1] = n
    mem[2] = v

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
    global input_mem
    global mem
    parseInput()

    print input_mem

    for i in range(100):
        for j in range(100):
            initMem(i, j)
            while executeStep():
                pass
            if mem[0] == 19690720:
                print (i, j, 100 * i + j)
                print mem
                return 1

if __name__ == '__main__':
    main()
