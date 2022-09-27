# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# explanation
# "([)]" <- this does not work, opening does not close in correct order
# as we are closing a parentheses, we are popping from the top of the stack
#


def isValid(s):
    if len(s) % 2 == 1:
        return False

    stack = []

    validator = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    for c in s:
        if c in validator:
            # if the stack isn't empty and the last item added is a opening bracket
            if stack and stack[-1] == validator[c]:
                # okay good we can start popping
                stack.pop()
            else:
                # no matching paren
                return False
        else:
            stack.append(c)
    res = True if not stack else False
    print(res)
    return res


s = "[((){()))})]"

isValid(s)

# # My solution without stacks
# # does not work on out of order items
# def isValid(s):
#     res = False
#     if len(s) % 2 == 1:
#         return False

#     sample = "()[]{}"

#     validator = {}
#     i = 0

#     while i < len(sample) - 1:
#         validator[sample[i]] = sample[i + 1]
#         i += 2

#     while i < len(s) - 1:
#         if validator[s[i]] == s[i + 1]:
#             res = True
#         else:
#             res = False
#         i += 2

#     print(res)
#     return res


# s = "()[]{}"

# isValid(s)
