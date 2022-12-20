
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


def getSumTopThree(input):
    input.sort(reverse=True)
    return sum(input[:3])


lines = readFile('input.txt')
elves = getElvesCarry(lines)
sum = getSumTopThree(elves)
print(sum)
