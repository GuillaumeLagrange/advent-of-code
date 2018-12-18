#!/bin/python3

file = open("input/XXX.txt", "r")

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
    for line in file:
        print(line)


def main():
    parseInput()


if __name__ == '__main__':
    main()
