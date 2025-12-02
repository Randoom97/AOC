from input import input

def calibrationValue(line: str):
    matches = [('zero', 0), ('one', 1), ('two', 2), ('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9),('0', 0), ('1', 1), ('2', 2), ('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9)]
    start = 0
    tensPlace = None
    while tensPlace == None and start < len(line):
        for match in matches:
            if line[start:].startswith(match[0]):
                tensPlace = match[1]
                break
        start += 1
    end = len(line)
    onesPlace = None
    while onesPlace == None and end >= 0:
        for match in matches:
            if line[:end].endswith(match[0]):
                onesPlace = match[1]
                break
        end -= 1
    return tensPlace*10 + onesPlace

total = 0
for line in input:
    total += calibrationValue(line)

print(total)