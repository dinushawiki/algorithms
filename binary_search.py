import math


class BinarySearch:
    def __init__(self, user_list, target):
        self.values = user_list
        self.value = target

    def search(self):
        return self.binary_search(self.values)

    def binary_search(self, values_to_check):
        if len(values_to_check) is 1:
            return False

        index_to_check = math.floor(len(values_to_check) / 2)
        print(index_to_check)
        if values_to_check[index_to_check] is self.value:
            return True
        if values_to_check[index_to_check] > self.value:
            print(values_to_check[:index_to_check])
            return self.binary_search(values_to_check[:index_to_check])
        if values_to_check[index_to_check] < self.value:
            print(values_to_check[index_to_check:])
            return self.binary_search(values_to_check[index_to_check:])


a = BinarySearch([1, 2, 3, 4, 5, 6], 6)
print(a.search())
