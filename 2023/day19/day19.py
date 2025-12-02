from input import workflowInput

def convertWorkflowInput(workflowInput: list[str]):
    workflows = {}
    for line in workflowInput:
        symbol = line[:line.find('{')]
        workflowStrings = line[line.find('{')+1:-1].split(',')
        workflowList = []
        for workflowString in workflowStrings:
            workflow = {}
            if workflowString.find(':') >= 0:
                workflow['condition'], workflow['symbol'] = workflowString.split(':')
            else:
                workflow['condition'] = "True"
                workflow['symbol'] = workflowString
            workflowList.append(workflow)
        workflows[symbol] = workflowList
    return workflows

workflows = convertWorkflowInput(workflowInput)
partsToProcess = []
partsToProcess.append(('in', {'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}))
acceptedParts = []
rejectedParts = []
while partsToProcess:
    state, partRange = partsToProcess.pop()
    if state == 'R':
        rejectedParts.append(partRange)
        continue
    if state == 'A':
        acceptedParts.append(partRange)
        continue
    workflow = workflows[state]
    for flow in workflow:
        condition = flow['condition']
        if(condition == 'True'):
            partsToProcess.append((flow['symbol'], partRange))
            continue
        symbol = condition[:1]
        comparison = condition[1:2]
        value = int(condition[2:])
        range = partRange[symbol]
        if comparison == '>':
            if not range[0] > value:
                if not range[1] > value:
                    continue
                newPartRange = partRange.copy()
                newPartRange[symbol] = (value+1, range[1]) 
                partsToProcess.append((flow['symbol'], newPartRange))
                partRange[symbol] = (range[0], value)
            else:
                partsToProcess.append((flow['symbol'], partRange))
                break
        if comparison == '<':
            if not range[1] < value:
                if not range[0] < value:
                    continue
                newPartRange = partRange.copy()
                newPartRange[symbol] = (range[0], value-1)
                partsToProcess.append((flow['symbol'], newPartRange))
                partRange[symbol] = (value, range[1])
            else:
                partsToProcess.append((flow['symbol'], partRange))
                break

print("accepted part ranges")
for part in acceptedParts:
    print(part)
totalCombinations = 0
for part in acceptedParts:
    totalCombinations += (part['x'][1]-part['x'][0]+1) * (part['m'][1]-part['m'][0]+1) * (part['a'][1]-part['a'][0]+1) * (part['s'][1]-part['s'][0]+1)
print(totalCombinations)
# print()
# print("rejected part ranges")
# for part in rejectedParts:
#     print(part)
# totalCombinations = 0
# for part in rejectedParts:
#     totalCombinations += (part['x'][1]-part['x'][0]+1) * (part['m'][1]-part['m'][0]+1) * (part['a'][1]-part['a'][0]+1) * (part['s'][1]-part['s'][0]+1)
# print(totalCombinations)
# print()
# print("expected accepted")
# print(167409079868000)

