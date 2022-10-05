# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]


# ( => ( or )
# left -1 left -1 right -1
# decision trees

# if n = 3
# 3 open 3 close
# cannot start with close
# close < open
# only add a closing parenthesis if close < open

def solution(n):

    res = []

    # what is path
    def backtrack(openN, closedN, path):
        # valid if open == close == n
        if openN == closedN == n:
            # join and append valid parens
            res.append(path)
            return

        # only add open parenthesis if open < n
        if openN < n:
            backtrack(openN + 1, closedN, path + "(")

        if closedN < openN:
            backtrack(openN, closedN + 1, path + ")")

    backtrack(0, 0, "")
    print(res)
    return res


n = 3
solution(n)
