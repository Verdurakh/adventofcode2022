
def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        return list(map(lambda s: s.strip(), lines))


def getElvesCarry(lines):
    currentElf = 0
    listOfElves = []
    listOfElves.append(0)
    for l in lines:
        if l == '':
            currentElf += 1
            listOfElves.append(0)
            continue
        listOfElves[currentElf] += int(l)
    return listOfElves


def getMaxValue(input):
    return max(input)


lines = readFile('input.txt')
elves = getElvesCarry(lines)
print(getMaxValue(elves))
