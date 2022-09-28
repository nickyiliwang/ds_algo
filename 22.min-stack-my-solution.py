# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.min = None
        self.next = None


class MinStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, val: int) -> None:
        # add item to the end of the list
        # new node has data of val on instantiation
        # instantiate Node class
        new_node = Node(val)

        if (self.isEmpty()):
            self.head = new_node
            self.head.min = self.head.data
            self.size += 1
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

        # tail_val = self.tail.data

        # curr_node.next is None when curr_node is the last node
        self.tail = prev_node
        prev_node.next = None
        self.size -= 1

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
            print(self.size)

    def top(self) -> int:
        if (self.isEmpty()):
            return None
        else:
            return self.head.data

    def getMin(self) -> int:
        if self.isEmpty():
            print("Stack Underflow")

        else:
            curr_node = self.head
            res = self.head.data
            while curr_node is not None:
                res = min(res, curr_node.data)
                curr_node = curr_node.next
            print(res)
            return res


my_stack = MinStack()
my_stack.push(4)
my_stack.push(2)
my_stack.push(3)
my_stack.push(-1)
my_stack.push(-2)

# my_stack.pop()
# my_stack.pop()
# my_stack.pop()


my_stack.getMin()
