def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


def containsDuplicates(word):
    for c in word:
        if word.count(c) > 1:
            return True


def checkLastThree(inputChars, inputLetter, position):
    sequence = ''
    for i in range(1, lettersToCheck):
        sequence += inputChars[position-i]
    sequence += inputLetter
    canBeMarker = False
    if sequence.count(inputLetter) == 1:
        canBeMarker = True
    if canBeMarker:
        if containsDuplicates(sequence):
            canBeMarker = False
    if canBeMarker:
        print('checking word ' + sequence)
    return canBeMarker


def findMarker(chars):
    i = 0
    for letter in chars:
        if i < lettersToCheck:
            i += 1
            continue

        if checkLastThree(chars, letter, i):
            print('letter ' + letter)
            print('index ' + str(i + 1))
            break
        i += 1


lettersToCheck = 14
lines = readFile("input.txt")
chars = lines.pop()
print(chars)
findMarker(chars)



