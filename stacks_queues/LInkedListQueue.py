class LinkedListIterator(object):
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item

    def hasnext(self):
        return self.current is not None


class LinkedListQueue:
    def __init__(self, head=None):
        self.head = head
        self.last = head

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

    def __iter__(self):
        return LinkedListIterator(self.head)

    def enque(self, data):
        new_node = self.Node(data)
        new_node.set_next(None)
        if self.last is None:
            self.last = self.head = new_node
            return
        last_node = self.last
        last_node.set_next(new_node)
        self.last = new_node

    def deque(self):
        current = self.head
        if current:
            self.head = current.get_next()

    def printList(self):
        list_to_print = []
        current = self.head
        while current is not None:
            list_to_print.append(current.get_data())
            current = current.get_next()
        print(list_to_print)


newList = LinkedListQueue()
newList.printList()
newList.enque(1)
newList.enque(2)
newList.enque(3)
newList.printList()
newList.deque()
newList.printList()

newList = LinkedListQueue()
newList.enque(1)
newList.enque(2)
newList.enque(3)
for item in newList:
    print(item)
