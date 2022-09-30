# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


# neetcode
# Time: O(1), Space: O(n)

def evalRPN(tokens):
    stack = []

    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "-":
            # we want to subtract the second from the first
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "/":
            # we want to divide the second from the first
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))

    return stack[0]


tokens = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens))


# # MY solution, pretty good if you ask me
# # this does not work if they keep adding operations
# # like: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# # going to neetcode

# import operator


# def evalRPN(tokens):
#     stack = []

#     operators = {
#         '+': operator.add,
#         '-': operator.sub,
#         '*': operator.mul,
#         '/': operator.truediv,
#     }

#     for i, c in enumerate(tokens):
#         if c not in operators:
#             stack.append(int(c))

#         # double ops
#         elif (i + 1) < len(tokens) and tokens[i + 1] in operators:
#             temp = int()
#             temp = operators[c](stack[-2], stack[-1])
#             stack.pop()
#             stack.pop()
#             stack.append(temp)
#         else:
#             if c == "/":
#                 temp = stack[0]
#                 for n in stack:
#                     temp = operators[c](temp, n)
#                 stack = [temp]
#             elif c == "+" or c == "-":
#                 temp = 0
#                 for n in stack:
#                     temp = operators[c](temp, n)
#                 stack = [temp]
#             elif c == "*":
#                 temp = 1
#                 for n in stack:
#                     temp = operators[c](temp, n)
#                 stack = [temp]

#     return int(stack[0])


# tokens = ["4", "13", "5", "/", "+"]
# print(evalRPN(tokens))
