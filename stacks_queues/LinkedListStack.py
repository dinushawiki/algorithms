class LinkedListStack:
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

        def set_next(self, new_next):
            self.next_node = new_next

    def push(self, data):
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


newList = LinkedListStack()
newList.push(1)
newList.push(2)
newList.push("hello")
newList.push(4)
print(newList.size())
newList.show_values()
print(newList.search(4))
newList.pop()
print(newList.size())
newList.show_values()
newList.push(4)
newList.show_values()