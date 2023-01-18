class MinStack:

    def __init__(self):
        # we need 2 stacks, one to keep track of the stack
        # the other for the minimum value in this stack for O(1) lookup
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            # non empty
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


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
