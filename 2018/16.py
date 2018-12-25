#!/bin/python3

file = open("input/16.txt", "r")

sequence = []
instructions = []

def addr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] + reg[b]
    return ret


def addi(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] + b
    return ret


def mulr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] * reg[b]
    return ret


def muli(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] * b
    return ret


def banr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] & reg[b]
    return ret


def bani(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] & b
    return ret


def borr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] | reg[b]
    return ret


def bori(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a] | b
    return ret


def setr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = reg[a]
    return ret


def seti(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    ret[c] = a
    return ret


def gtir(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    if a >= reg[b]:
        ret[c] = 1
    else:
        ret[c] = 0
    return ret


def gtri(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    if reg[a] >= b:
        ret[c] = 1
    else:
        ret[c] = 0
    return ret


def gtrr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    if reg[a] >= reg[b]:
        ret[c] = 1
    else:
        ret[c] = 0
    return ret


def eqir(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    if a == reg[b]:
        ret[c] = 1
    else:
        ret[c] = 0
    return ret


def eqri(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    if reg[a] == b:
        ret[c] = 1
    else:
        ret[c] = 0
    return ret


def eqrr(reg, arg):
    ret = reg.copy()
    [a, b, c] = arg
    if reg[a] == reg[b]:
        ret[c] = 1
    else:
        ret[c] = 0
    return ret


def parseInput():
    global instructions
    global sequence
    instructions = [
        addr, addi,
        mulr, muli,
        banr, bani,
        borr, bori,
        setr, seti,
        gtir, gtri, gtrr,
        eqir, eqri, eqrr,
    ]

    while True:
        line = file.readline().strip()
        if "Before" not in line:
            break
        before = eval("".join(line.split(" ")[1::]))
        line = file.readline().strip()
        args = eval("[" + ", ".join(line.split(" ")) + "]")
        line = file.readline().strip()
        after = eval("".join(line.split(" ")[1::]))
        file.readline()

        sequence.append((before, args, after))


def main():
    global instructions
    global sequence
    instructionsNb = []
    sequenceNb = []
    parseInput()
    instructionsOpCodes = [None for i in range(len(instructions))]
    for i, element in enumerate(sequence):
        nb = [False for i in range(len(instructions))]
        n = 0
        for j, f in enumerate(instructions):
            if f(element[0], element[1][1::]) == element[2]:
                n += 1
                nb[j] = True
        instructionsNb.append(n)
        sequenceNb.append(nb)
    print(instructionsNb)

    for i, instr in enumerate(instructionsNb):
        if instr == 1:
            print("MATCH FOUND")
            instructionIdx = sequenceNb[i].index(True)
            instructionsOpCodes[sequence[i][1][0]] = instructions[instructionIdx]
            for j in range(len(sequence)):
                if sequenceNb[j][instructionIdx] is True:
                    if sequence[i][1][0] == sequence[j][1][0]:
                        instructionsNb[j] = 0
                        sequenceNb[j] = [False for i in range(len(instructions))]
                    else:
                        instructionsNb[j] -= 1
                    sequenceNb[j][instructionIdx] = False

    print(instructionsOpCodes)
    print(instructionsNb)
    for i, instr in enumerate(instructionsNb):
        if instr == 2:
            print("MATCH FOUND")
            instructionIdx = sequenceNb[i].index(True)
            instructionIdx = sequenceNb[i][instructionIdx + 1::].index(True)
            instructionsOpCodes[sequence[i][1][0]] = instructions[instructionIdx]
            for j in range(len(sequence)):
                if sequenceNb[j][instructionIdx] is True:
                    if sequence[i][1][0] == sequence[j][1][0]:
                        instructionsNb[j] = 0
                        sequenceNb[j] = [False for i in range(len(instructions))]
                    else:
                        instructionsNb[j] -= 1
                    sequenceNb[j][instructionIdx] = False

    print(instructionsOpCodes)
    print(instructionsNb)
    for i, instr in enumerate(instructionsNb):
        if instr == 2:
            print("MATCH FOUND")
            instructionIdx = sequenceNb[i].index(True)
            #  instructionIdx = sequenceNb[i][instructionIdx + 1::].index(True)
            instructionsOpCodes[sequence[i][1][0]] = instructions[instructionIdx]
            for j in range(len(sequence)):
                if sequenceNb[j][instructionIdx] is True:
                    if sequence[i][1][0] == sequence[j][1][0]:
                        instructionsNb[j] = 0
                        sequenceNb[j] = [False for i in range(len(instructions))]
                    else:
                        instructionsNb[j] -= 1
                    sequenceNb[j][instructionIdx] = False

    print(instructionsOpCodes)
    print(instructionsNb)



if __name__ == '__main__':
    main()
