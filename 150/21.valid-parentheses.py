class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        validator = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            if p in validator:
                if len(stack) == 0 or stack.pop() != validator[p]:
                    return False
            else:
                stack.append(p)

        if len(stack) > 0:
            return False

        return True
