class Node:

    def __init__(self, data=None):
        self.data = data
        self.min = None
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def displayTail(self) -> None:
        if self.isEmpty():
            return None

        else:
            return self.tail.data

    def push(self, val: int) -> None:
        new_node = Node(val)

        if (self.isEmpty()):
            self.head = new_node
            self.head.min = self.head.data
            self.size += 1
            self.tail = new_node
            return

        # list has one item
        elif self.tail is None:
            self.tail = new_node
            self.head.next = new_node
            self.head.next.min = min(self.head.min, self.head.next.data)
            self.size += 1
            return

        # list has multiple items
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            print('added', new_node.data)
            print('size', self.size)
            return

    def pop(self) -> None:
        if (self.isEmpty()):
            self.head = None
            return None

        # 1 item
        if self.tail is None:
            self.head = None
            self.size -= 1

        # 2 items, remove tail
        if self.head.next is self.tail:
            self.tail = None
            self.head.next = None
            self.size -= 1

        # multiple items
        prev_node = None
        # Start from head Node
        curr_node = self.head
        # Traverse to the last Node
        while curr_node.next is not None:
            prev_node = curr_node
            curr_node = curr_node.next

        self.tail = prev_node
        prev_node.next = None
        self.size -= 1

    def popleft(self):
        if self.isEmpty():
            return None

        tmp = self.head

        self.head = self.head.next
        self.size -= 1
        return tmp

    def display(self):
        if self.isEmpty():
            print("Stack Underflow")

        else:
            curr_node = self.head
            elements = []
            while curr_node is not None:
                elements.append(curr_node.data)
                curr_node = curr_node.next
            print(elements)
            print("size", self.size)

    def top(self) -> int:
        if (self.isEmpty()):
            return None
        else:
            return self.head.data


class MinStack:

    def __init__(self):
        self.stack = Stack()
        self.minStack = Stack()

    def push(self, val: int) -> None:
        self.stack.push(val)

        if self.minStack.isEmpty():
            self.minStack.push(val)

        else:
            minStackVal = self.minStack.displayTail()
            self.minStack.push(min(val, minStackVal))
        self.stack.display()
        self.minStack.display()

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack.top()

    def getMin(self) -> int:
        return self.minStack.displayTail()


my_stack = MinStack()
my_stack.push(4)
my_stack.push(2)
my_stack.push(3)
my_stack.push(-1)
my_stack.push(-2)
my_stack.push(5)
my_stack.push(-20)
my_stack.push(5)
minVal = my_stack.getMin()
print("minVal:", minVal)