def readFile(filename):
    with open(filename) as f:
        result = f.readlines()
        return list(map(lambda s: s.strip(), result))


class Folder:
    def __init__(self, name, parent):
        self.folders = []
        self.files = []
        self.name = name
        self.size = 0
        self.parent = parent


class File:
    size = 0
    name = ''
    parent = {}


def calculuateMap(inputRoot):
    currentPosition = inputRoot
    for command in lines:
        split = command.split()
        if split[0] == '$':
            if split[1] == 'cd':
                if split[2] == '/':
                    print('go to root')
                    currentPosition = inputRoot
                    continue
                elif split[2] == '..':
                    print('Go back from '+currentPosition.name + ' to ' + currentPosition.parent.name)
                    currentPosition = currentPosition.parent
                else:
                    print('move to ' + split[2])
                    currentPosition = next((x for x in currentPosition.folders if x.name == split[2]), None)

        elif split[0] == 'dir':
            if not any(x.name == split[1] for x in currentPosition.folders):
                print('adding folder '+split[1] + ' to folder ' + currentPosition.name)
                newFolder = Folder(split[1], currentPosition)
                currentPosition.folders.append(newFolder)
        else:
            file = File()
            file.name = split[1]
            file.size = int(split[0])
            file.parent = currentPosition
            currentPosition.files.append(file)
            #currentPosition.size += file.size
            print('added file ' + file.name + ' size ' + str(file.size) + ' to ' + currentPosition.name)


def calculateFolderSizes(inputRoot: Folder):
    sum = 0

    if len(inputRoot.files) > 0:
        sum= sumFileSize(inputRoot.files)

    for fold in inputRoot.folders:
        returnValue = calculateFolderSizes(fold)
        fold.size += returnValue
        sum += returnValue
    return sum


def sumFileSize(files):
    sum = 0
    for file in files:
        sum += file.size
    return sum


def calculateTotalOfFoldersLessThan10(inputRoot: Folder):
    sum = 0

    for fold in inputRoot.folders:
        returnValue = calculateTotalOfFoldersLessThan10(fold)
        sum += returnValue

    if inputRoot.size <= 100000:
        sum += inputRoot.size

    return sum


lines = readFile("input.txt")
#print(lines)

root = Folder('/', {})
calculuateMap(root)
root.size = calculateFolderSizes(root)
print(root.size)
combined= calculateTotalOfFoldersLessThan10(root)
print(combined)
