# This could be solved with a stack, or backtracking
def solution(n):

    res = []

    def backtrack(openN, closedN, variation):
        # valid if open == close == n
        if openN == closedN == n:
            # join and append valid parens
            res.append(variation)
            return

        # only add open parenthesis if open < n
        if openN < n:
            backtrack(openN + 1, closedN, variation + "(")

        if closedN < openN:
            backtrack(openN, closedN + 1, variation + ")")

    backtrack(0, 0, "")
    print(res)
    return res


n = 3
solution(n)
