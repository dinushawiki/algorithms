import random


class Item:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __eq__(self, other):
        return self.value == other.value

    def get_value(self):
        return self.value


class Shuffling:
    def __init__(self, values):
        self.values = values

    def shuffle(self):
        n = len(self.values)
        for i in range(n):
            r = random.randint(0, i)
            self.exchange(i, r)
        return self.values

    def exchange(self, a, b):
        swap = self.values[a]
        self.values[a] = self.values[b]
        self.values[b] = swap


items = [Item(0), Item(1), Item(2), Item(3), Item(4), Item(5), Item(6), Item(7), Item(8), Item(9)]
array_to_shuffle = Shuffling(items)
shuffled = array_to_shuffle.shuffle()
[print(item.get_value()) for item in shuffled]
