from collections import deque


def isValid(s):
    if len(s) % 2 != 0:
        return False

    stack = deque()

    validator = {"}": "{", ")": "(", "]": "["}

    for p in s:
        if p in validator:
            # if the stack isn't empty and the last item added is a opening bracket
            if not stack or stack.pop() != validator[p]:
                return False
        else:
            stack.append(p)

    # need to double check if the stack is empty in case: "(("
    return True if not stack else False


s = "([)]"

isValid(s)