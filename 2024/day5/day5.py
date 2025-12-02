from input import rules, reports

ruleMap = {}
for rule in rules:
    if rule[0] not in ruleMap:
        ruleMap[rule[0]] = set()
    ruleMap[rule[0]].add(rule[1])

def isValid(report):
    processed = set()
    for number in report:
        if number in ruleMap and len(processed.intersection(ruleMap[number])) != 0:
            return False
        processed.add(number)
    return True

def makeValid(report):
    numbers = set()
    for number in report:
        numbers.add(number)

    sortableReport = []
    for number in report:
        if number not in ruleMap:
            sortableReport.append((len(report), number))
        else:
            sortableReport.append(((len(report) - len(numbers.intersection(ruleMap[number]))), number))
    sortableReport.sort()
    fixedReport = []
    for entry in sortableReport:
        fixedReport.append(entry[1])
    
    return fixedReport

part1 = 0
part2 = 0
for report in reports:
    if isValid(report):
        part1 += report[len(report)//2]
    else:
        validReport = makeValid(report)
        part2 += validReport[len(validReport)//2]
print(part1)
print(part2)