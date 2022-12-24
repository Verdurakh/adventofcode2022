def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


def charToScore(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38


lines = readFile("input.txt")
#print(lines)
score = 0

i = iter(lines)
chunk = list(zip(i, i, i))
print(chunk)


for group in chunk:
    strings = []
    for line in group:
        strings.append(line)
    letter = set(group[0]) & set(group[1]) & set(group[2])
    score += charToScore(letter.pop())

print(score)

