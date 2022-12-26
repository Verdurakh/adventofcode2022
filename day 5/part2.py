def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        #return result
        return list(map(lambda s: s.replace('\n',''), result))


def extractState(inputLines):
    state = []
    for l in inputLines:
        if l == '' or l[1].strip().isnumeric():
            break
        state.append(removeJunk(l))
    return state


def removeJunk(inputString):
    return inputString.replace('[', '').replace(']', '').replace(' ','-')


def stateIntoArrays(inputState):
    array=[]
    for letter in inputState:
        letter=letter.replace('----','-')
        splitted = letter.split('-')
        index=0
        for l in splitted:
            if len(array) <= index:
                array.append('')
            if l != '':
                array[index] += l
            index +=1

    return array


def extractInstructions(inputLines):
    result = []
    reached=False
    for l in inputLines:
        if l == '':
            reached = True
            continue
        if reached:
            result.append(l)
    return result


def runInstructions(inputState, inputInstructions):
    #print('start running instructions')
    for instruction in inputInstructions:
        runInstruction(inputState,instruction)


def runInstruction(inputState, inputInstrution):
    splitted = inputInstrution.split()
    number= int(splitted[1])
    fromLocation = int(splitted[3])-1
    toLocation = int(splitted[5])-1
    #print(inputState)
    #print('move ' + str(number) + ' from ' + str(fromLocation)+ ' to ' +str(toLocation))
    #for count in range(0,number):
    removedItem=inputState[fromLocation].split()[0][0:number]
    #print(removedItem)
    inputState[fromLocation]=inputState[fromLocation][number:]
    inputState[toLocation]=removedItem+inputState[toLocation]


def getMessage(inputState):
    newStr=''
    for letter in inputState:
        newStr+=letter[0]
    return newStr

lines = readFile("input.txt")
#print(lines)
state = extractState(lines)
#print(state)
arrays= stateIntoArrays(state)
#print(arrays)
instructions = extractInstructions(lines)
#print(instructions)
runInstructions(arrays,instructions)
print(arrays)
print(getMessage(arrays))





