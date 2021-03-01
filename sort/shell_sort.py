class Item:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def get_value(self):
        return self.value


class ShellSort:
    def __init__(self, values):
        self.values = values

    def sort(self):
        n = len(self.values)
        h = 1
        while h < n:
            h = (3 * h) + 1

        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h:
                    if self.less(self.values[j], self.values[j - h]):
                        self.exchange(j, j - h)
                        j -= h
                    else:
                        break
            h = int(h / 3)
        return self.values

    def exchange(self, i, j):
        swap = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = swap

    @staticmethod
    def less(a, b):
        return a.__lt__(b)


items = [Item(2), Item(1), Item(4), Item(3), Item(0), Item(6), Item(2), Item(7), Item(8), Item(9), Item(7)]
array_to_sort = ShellSort(items)
sorted_array = array_to_sort.sort()
[print(item.get_value()) for item in sorted_array]
