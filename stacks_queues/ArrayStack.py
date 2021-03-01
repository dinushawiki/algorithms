import numpy
import math


class ArrayStack:
    def __init__(self, numItems):
        self.items = numpy.empty(numItems, dtype=object)
        self.index = 0

    def isEmpty(self):
        print(self.items.size)
        return self.index == 0

    def push(self, data):
        if self.index == len(self.items):
            self.resize(2 * len(self.items))
        self.items[self.index] = data
        self.index += 1

    def resize(self, length):
        copy = numpy.empty(length, dtype=object)
        for i in range(len(self.items)):
            copy[i] = self.items[i]
        self.items = copy

    def resize_pop(self, length):
        copy = numpy.empty(length, dtype=object)
        for i in range(length):
            copy[i] = self.items[i]
        self.items = copy

    def pop(self):
        if self.index > 0:
            self.items[self.index] = None
            if self.index > 0 and self.index <= (len(self.items) / 4):
                self.resize_pop(math.ceil(len(self.items) / 2))
            self.index -= 1


test = ArrayStack(1)
print(test.isEmpty())
test.push(1)
print(test.isEmpty())
test.push(2)
print(test.isEmpty())
test.push(3)
print(test.isEmpty())
test.push(4)
print(test.isEmpty())
test.push(5)
print(test.isEmpty())
test.push(6)
print(test.isEmpty())
test.pop()
print(test.isEmpty())
test.pop()
print(test.isEmpty())
test.pop()
print(test.isEmpty())
test.pop()
print(test.isEmpty())
test.pop()
print(test.isEmpty())