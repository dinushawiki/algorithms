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

        def set_next(self, node):
            self.next_node = node

    def push(self, data):
        node = self.Node(data)
        node.set_next(self.head)
        self.head = node

    def pop(self):
        current = self.head
        self.head = current.get_next()
        return current.get_data()

    def print_list(self):
        list_to_print = []
        current = self.head
        while current is not None:
            list_to_print.append(current.get_data())
            current = current.get_next()
        print(list_to_print)


def dijksta_algo(expression):
    val_stack = LinkedListStack()
    ops_stack = LinkedListStack()

    for item in expression:
        if item == "(":
            None
        elif item == "+":
            ops_stack.push(item)
        elif item == "*":
            ops_stack.push(item)
        elif item == ")":
            op = ops_stack.pop()
            if op == "+":
                val_stack.push(val_stack.pop() + val_stack.pop())
            if op == "*":
                val_stack.push(val_stack.pop() * val_stack.pop())
        else:
            val_stack.push(float(item))
    return val_stack.pop()


evaluate = "(1+((2+3)*(4*5)))"
print(dijksta_algo(evaluate))
