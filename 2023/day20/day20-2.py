from input import input

def parseModules(moduleStrings: list[str]):
    modules = {}
    for line in moduleStrings:
        module = {}
        label, outputs = line.split('->')
        label = label.strip()
        outputs = "".join(outputs.split()).split(',')
        module['outputs'] = outputs
        if label[:1] == '%':
            label = label[1:]
            module['type'] = '%'
            module['state'] = 0
        elif label[:1] == '&':
            label = label[1:]
            module['type'] = '&'
            module['lastFrom'] = {}
        else:
            module['type'] = 'b'
        modules[label] = module
    for label in modules:
        module = modules[label]
        for outputLabel in module['outputs']:
            if outputLabel in modules and modules[outputLabel]['type'] == '&':
                modules[outputLabel]['lastFrom'][label] = 0
    return modules

def pushButton(modules):
    rsHistory = []
    toProcess = []
    toProcess.append((0, 'broadcaster', 'button'))
    while toProcess:
        signal, label, fromLabel = toProcess.pop(0)
        if label not in modules:
            continue
        module = modules[label]
        if module['type'] == '%':
            if signal:
                continue
            module['state'] = int(not module['state'])
            for output in module['outputs']:
                toProcess.append((module['state'], output, label))
        elif module['type'] == '&':
            module['lastFrom'][fromLabel] = signal
            toSend = 1
            if all([module['lastFrom'][key] for key in module['lastFrom']]):
                toSend = 0
            for output in module['outputs']:
                toProcess.append((toSend, output, label))
        else:
            for output in module['outputs']:
                toProcess.append((signal, output, label))
        if label == 'rs' and signal:
            rsHistory.append(modules[label]['lastFrom'].copy())
    return rsHistory

modules = parseModules(input)

for i in range(10000):
    rsHistory = pushButton(modules)
    if rsHistory:
        print(str(i) +": "+ str(rsHistory))



