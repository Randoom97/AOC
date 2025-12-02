import math

class Monkey:
    def __init__(self, items: list[int], operation, test, trueTarget: int, falseTarget: int):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.inspectionCount = 0

    def inspection(self):
        self.inspectionCount += 1
        prevItem = self.items.pop(0)
        newItem = self.operation(prevItem)
        item = newItem % math.lcm(17, 3, 5, 7, 11, 19, 2, 13)
        # item = newItem % math.lcm(23, 19, 13, 17)
        target = self.trueTarget if item % self.test == 0 else self.falseTarget
        return item, target

    def __repr__(self):
        return str(self.inspectionCount)
        # return self.items.__str__()