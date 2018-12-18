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
    parseInput()
    for i, element in enumerate(sequence):
        nb = 0
        for f in instructions:
            if f(element[0], element[1][1::]) == element[2]:
                nb += 1
        instructionsNb.append(nb)
    a = 0
    for n in instructionsNb:
        if n >=3:
            a += 1
    print(a)




if __name__ == '__main__':
    main()
