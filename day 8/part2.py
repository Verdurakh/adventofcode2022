def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


def inputToTwoDArray(inputLines):
    list=[]

    for line in inputLines:
        newList=[]
        for ch in line:
            newList.append(int(ch))
        list.append(newList)
    return list


def isAtEdge(inputList, x, y):
    if x == 0 or y == 0:
        return True

    if x == len(inputList[0])-1 or y == len(inputList)-1:
        return True

    return False


def calculateScore(inputList, inputy, inputx):
    if isAtEdge(inputList, inputx, inputy):
        return True

    value = inputList[inputy][inputx]

    scoreLeft=0

    for x in range(1, inputx+1):
        scoreLeft += 1
        if isAtEdge(inputList,inputx-x,inputy) or inputList[inputy][inputx-x] >= value:
            break

    scoreRight=0
    for x in range(1, len(inputList[inputy])+1):
        scoreRight += 1
        if isAtEdge(inputList,inputx+x,inputy) or inputList[inputy][inputx+x] >= value:
            break


    scoreUp = 0
    for y in range(1, inputy+1):
        scoreUp += 1
        if isAtEdge(inputList,inputx,inputy-y) or inputList[inputy - y][inputx] >= value:
            break


    scoreDown= 0
    for y in range(1, len(inputList)+1):
        scoreDown += 1
        if isAtEdge(inputList,inputx, inputy+y) or inputList[inputy + y][inputx] >= value:
            break


    score = scoreLeft * scoreUp * scoreRight * scoreDown
    #print(str(value) + ' score '+str(score) + '. x: ' + str(inputx) + ' y: '+str(inputy))
    return score


def getHighestScore(inputList):
    sum =0
    for y in range(len(inputList)):
        for x in range(len(inputList[0])):
            result= calculateScore(inputList,y,x)
            if(result > sum):
                sum = result
    return sum


def printWood(inputList):
    for line in inputList:
        print(line)

lines = readFile("input.txt")
#print(printWood(lines))
list= inputToTwoDArray(lines)
#print(list)
print(getHighestScore(list))
#print(calculateScore(list,1,2))

