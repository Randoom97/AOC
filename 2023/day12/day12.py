from functools import cache

from input import input

def groupsToString(group:list[int]):
    if len(group) == 0:
        return ''
    return ','.join([str(x) for x in group])

def groupsFromString(groupStr:str):
    if groupStr == '':
        return []
    return [int(x) for x in groupStr.split(',')]

@cache
def validCount(springs:str, groupsStr:str):
    groups = groupsFromString(groupsStr)
    if len(springs) == 0:
        return 1 if len(groups) == 0 else 0

    current = springs[0]
    if current == '#':
        if len(groups) == 0 or len(springs) < groups[0]:
            return 0
        if '.' in springs[:groups[0]]:
            return 0
        if len(springs) > groups[0]:
            if '#' == springs[groups[0]]:
                return 0
            if '?' == springs[groups[0]]:
                return validCount(springs[groups[0]+1:].lstrip('.'), groupsToString(groups[1:]))
        return validCount(springs[groups[0]:].lstrip('.'), groupsToString(groups[1:]))
    elif current == '.':
        return validCount(springs[1:].lstrip('.'), groupsStr)
    else:
        return validCount('#'+springs[1:], groupsStr) + validCount(springs[1:].lstrip('.'), groupsStr)



total = 0
for index, line in enumerate(input):
    parts = line.split()
    
    # configuration = parts[0]
    # validation = parts[1]

    configuration = '?'.join(5*[parts[0]])
    validation = ','.join(5*[parts[1]])
    
    configurations = validCount(configuration, validation)
    # print(configurations)
    total += configurations
print(total)