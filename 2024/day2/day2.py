from input import input

def isSafe(report):
    if report[0] == report[1]:
        return False
    increasing = report[0] < report[1]
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        diffIncreasing = diff > 0
        if diffIncreasing != increasing:
            return False
    return True

totalSafe = 0
for report in input:
    if isSafe(report):
        totalSafe += 1
    else:
        for i in range(len(report)):
            reportCopy = report.copy()
            reportCopy.pop(i)
            if isSafe(reportCopy):
                totalSafe += 1
                break

print(totalSafe)
