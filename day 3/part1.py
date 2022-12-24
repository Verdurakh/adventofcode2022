def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


def charToScore(char):
    if(char.islower()):
        return ord(char) - 96
    return ord(char) - 38


lines = readFile("input.txt")
#print(lines)
score = 0
for line in lines:
    size = int(len(line) / 2)
    one = line[0: size]
    two = line[size: size + size]
    intersect = set(one) & set(two)
    score += charToScore(intersect.pop())

print(score)

