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


def isVisible(inputList, inputy, inputx):
    if isAtEdge(inputList, inputx, inputy):
        return True

    value = inputList[inputy][inputx]

    visible = True
    visibleLeft=True
    visibleRight=True
    for x in range(0,inputx):
        if x == inputx:
            continue
        if inputList[inputy][x] >= value:
            visibleLeft = False
            break
    for x in range(inputx,len(inputList[inputy])):
        if x == inputx:
            continue
        if inputList[inputy][x] >= value:
            visibleRight = False
            break

    visibleUp = True
    for y in range(0, inputy):
        if y == inputy:
            continue
        if inputList[y][inputx] >= value:
            visibleUp = False
            break

    visibleDown= True
    for y in range(inputy,len(inputList)):
        if y == inputy:
            continue
        if inputList[y][inputx] >= value:
            visibleDown = False
            break

    visible = visibleLeft or visibleUp or visibleRight or visibleDown
    #print(str(value) + ' visible '+str(visible) + '. x: ' + str(inputx) + ' y: '+str(inputy))
    return visible


def countVisible(inputList):
    sum =0
    for y in range(len(inputList)):
        for x in range(len(inputList[0])):
            if isVisible(inputList,y,x):
                sum += 1
    return sum


def printWood(inputList):
    for line in inputList:
        print(line)

lines = readFile("input.txt")
#print(printWood(lines))
list= inputToTwoDArray(lines)
#print(list)
print(countVisible(list))
#isVisible(list,1,3)

