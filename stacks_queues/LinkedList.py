class LinkedList:
    def __init__(self, head=None):
        self.head = head

    class Node:
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def set_data(self, data):
            self.data = data

        def set_next(self, new_next):
            self.next_node = new_next

    def insert(self, data):
        new_node = self.Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.set_next()
        else:
            previous.set_next(current.get_next())

    def pop(self):
        current = self.head
        if current:
            self.head = current.get_next()

    def show_values(self):
        current = self.head
        items = ""
        while current:
            items = items + "," + str(current.get_data())
            current = current.get_next()
        print(items)


newList = LinkedList()
newList.insert(1)
newList.insert(2)
newList.insert(3)
newList.insert(4)
print(newList.size())
newList.show_values()
print(newList.search(4))
newList.pop()
print(newList.size())
newList.show_values()
newList.insert(4)
newList.show_values()