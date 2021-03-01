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


class InsertionSort:
    def __init__(self, values):
        self.values = values

    def sort(self):
        n = len(self.values)
        for i in range(n):
            j = i
            while j > 0:
                if self.less(self.values[j], self.values[j - 1]):
                    self.exchange(j, j - 1)
                    j -= 1
                else:
                    break
        return self.values

    def exchange(self, i, j):
        swap = self.values[i]
        self.values[i] = self.values[j]
        self.values[j] = swap

    @staticmethod
    def less(a, b):
        return a.__lt__(b)


items = [Item(2), Item(1), Item(4), Item(3), Item(0)]
array_to_sort = InsertionSort(items)
sorted_array = array_to_sort.sort()
[print(item.get_value()) for item in sorted_array]
