#!/bin/python3

currentId = "0"
asleepHour = 0
asleepMin = 0
guards = {}

file = open("input/4.txt", "r")

def parseSentence(sentence):
    if sentence[0] == 'G':
        return(sentence.split(" ")[1][1::])
    return sentence[0]

def parseLine(line):
    [rawDate, sentence] = line.split("]")
    rawDate = rawDate[1::]
    sentence = sentence[1:-1]
    [rawDay, rawHour] = rawDate.split(" ")
    [year, month, day] = rawDay.split("-")
    [hour, minute] = rawHour.split(":")
    ret = (int(year), int(month), int(day), int(hour), int(minute), parseSentence(sentence))
    return ret

def printGuardSleepingTime(guardId):
    global guards
    print(guards[guardId])

def updateSleepingTime(hour, minute):
    global guards
    global asleepHour
    global asleepMin
    if asleepHour < hour:
        while asleepMin < 59:
            slot = guards[currentId]
            slot[str(asleepHour)][asleepMin] = slot[str(asleepHour)][asleepMin] + 1
            asleepMin = asleepMin + 1
        asleepMin = 0
        asleepHour = hour

    while asleepMin < minute:
        slot = guards[currentId]
        slot[str(asleepHour)][asleepMin] = slot[str(asleepHour)][asleepMin] + 1
        asleepMin = asleepMin + 1
    asleepHour = asleepHour + 1

def processLine(parsedLine):
    global currentId
    global asleepHour
    global asleepMin
    if parsedLine[-1] == 'f':
        asleepHour = parsedLine[3]
        asleepMin = parsedLine[4]
    elif parsedLine[-1] == 'w':
        updateSleepingTime(parsedLine[3], parsedLine[4])
    else:
        currentId = parsedLine[-1]
        if currentId not in guards:
            guards[currentId] = {'23': [0] * 60, '0': [0] * 60}

# Strategy 1
def findMostAsleepGuard():
    global guards
    maxIndex = ""
    maxSleptTotal = 0
    for i, guard in guards.items():
        print(i, guard)
        sleptTotal = 0
        for hourValue, hourArray in guard.items():
            for minuteSlept in hourArray:
                sleptTotal = sleptTotal + minuteSlept
        print(sleptTotal)
        if sleptTotal > maxSleptTotal:
            maxSleptTotal = sleptTotal
            maxIndex = i

    return maxIndex


def findMostAsleepMinute(guardId):
    global guards
    guard = guards[guardId]
    maxHour = 0
    maxMinute = 0
    maxVal = 0
    for hour, hourArray in guard.items():
        for i, val in enumerate(hourArray):
            if val > maxVal:
                maxVal = val
                maxMinute = i
                maxHour = hour
    return maxHour, maxMinute

# Strategy 2
def findAbsoluteMostAsleepMinute():
    global guards
    maxIndex = ""
    maxMin = 0
    maxVal = 0
    for i, guard in guards.items():
        for hourValue, hourArray in guard.items():
            for minute, val in enumerate(hourArray):
                if val > maxVal:
                    maxVal = val
                    maxIndex = i
                    maxMin = minute
    print(guards[maxIndex])
    print(maxIndex, maxMin, maxVal)
    return maxIndex, maxMin


def main():
    parsedLines = []
    for line in file:
        parsedLine = parseLine(line)
        parsedLines.append(parsedLine)

    parsedLines.sort()
    for parsedLine in parsedLines:
        processLine(parsedLine)

    maxAsleep = findMostAsleepGuard()
    maxHour, maxMinute = findMostAsleepMinute(maxAsleep)

    print("Strategy 1 answer is %d" % (int(maxAsleep) * maxMinute))

    guard, minute = findAbsoluteMostAsleepMinute()

    print("Strategy 2 answer is %d" % (int(guard) * minute))



if __name__ == '__main__':
    main()
