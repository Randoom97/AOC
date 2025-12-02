from input import input

class Directory:
    def __init__(self):
        self.files = {}
        self.directories={}

    def __str__(self):
        return "files: "+self.files.__repr__()

    def __repr__(self):
        return self.__str__()

def directorySize(directory: Directory):
    sum = 0
    for subDir in directory.directories.values():
        sum += directorySize(subDir)
    for file in directory.files.values():
        sum += file
    return sum

directories = {'/': Directory()}
currentDir = Directory()
workingDir = ['/']
for line in input:
    if line.startswith('$ cd'):
        target = line[5:]
        if target == '..':
            workingDir.pop()
        elif target == '/':
            workingDir = ['/']
        else:
            workingDir.append(target)
        currentDir = directories.get('/'.join(workingDir))
    elif line.startswith('$ ls'):
        # currentDir = Directory()
        # directories['/'.join(workingDir)] = currentDir
        continue
    elif line.startswith('dir'):
        dirName = line[4:]
        if dirName in currentDir.directories.keys():
            continue
        directory = Directory()
        currentDir.directories[dirName] = directory
        directories['/'.join(workingDir)+'/'+dirName] = directory
    else:
        fileInfo = line.split(' ')
        currentDir.files[fileInfo[1]] = int(fileInfo[0])

directorySizes = {}
for key in directories.keys():
    directorySizes[key] = directorySize(directories.get(key))
# print(directorySizes)

currentSize = directorySizes.get('/')
target = currentSize-40000000

sizes = list(directorySizes.values())
sizes.sort()
for size in sizes:
    if size > target:
        break
print(size)