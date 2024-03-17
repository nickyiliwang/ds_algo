# Stacks
# First In Last out, last in first out (LIFO)
# Think Execution stacks
# Insertion and Deletion happens on the same end


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)

        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            self.first = newNode
            self.first.next == temp
        self.size += 1
        return self.size

    # pop is not working properly
    def pop(self):
        if self.first == None:
            return None

        if self.first == self.last:
            self.last = None

        temp = self.first
        self.first = self.last.next
        self.size -= 1
        return temp.value


myStack = Stack()

print(myStack.size)
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack.size)


print(myStack.pop(), "popped")
print(myStack.pop(), "popped")

print(myStack.size)
