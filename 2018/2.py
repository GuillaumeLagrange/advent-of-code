#!/bin/python3

data = [x.strip() for x in open("input/2.txt", "r").readlines()]


def main():
    two = 0
    three = 0
    for line in data:
        letters = dict.fromkeys(line, 0)
        for letter in line:
            letters[letter] += 1
        if 2 in letters.values():
            two += 1
        if 3 in letters.values():
            three += 1
    print("two is %d three is %d answer is %d" % (two, three, two * three))

    for line in data:
        for string in data:
            diff = 0
            for i in range(len(line)):
                if line[i] != string[i]:
                    diff += 1
            if diff == 1:
                ans = [x for i, x in enumerate(line) if string[i] == x]
                print("part two answer is %s" % "".join(ans))
                return



if __name__ == '__main__':
    main()
