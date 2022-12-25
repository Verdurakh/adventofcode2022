def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


def contains(first, second):
    inX = int(first[0])
    inY = int(first[1])
    outX  = int(second[0])
    outY = int(second[1])
    if inX >= outX and inY <= outY:
        return True
    return False


lines = readFile("input.txt")
#print(lines)

score = 0
for line in lines:
    #print(line)
    split = line.split(',')
    first = split[0].split('-')
    second = split[1].split('-')
    addScore = False
    if contains(first, second):
        addScore = True
        #print(str(second)+' contains ' + str(first))
    if contains(second, first):
        addScore = True
        #print(str(first)+' contains ' + str(second))
    if addScore:
        score += 1

print(score)
