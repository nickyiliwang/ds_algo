class MonotonicDecreasingStack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) == 0 or value < self.stack[-1]:
            self.stack.append(value)
        else:
            raise ValueError("New value must be less than current top.")

    def pop(self):
        if len(self.stack) == 0:
            raise ValueError("Stack is empty.")
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            raise ValueError("Stack is empty.")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# A stack is a data structure that follows the Last In, First Out (LIFO) principle, meaning the last element added to the stack is the first one to be removed. A monotonic decreasing stack is a stack in which the elements are always in decreasing order, so the element that is added last will have a lower value than the one that was added before it.

# You can use this class to create an instance of the stack and use the push, pop and top methods to add, remove, and check top element respectively.

# You can also use the is_empty method to check whether the stack is empty or not.