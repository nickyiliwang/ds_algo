def solution(n):

    res = []

    def backtrack(open, closed, variation):
        if open == closed == n:
            res.append(variation)
            return

        if open < n:
            backtrack(open + 1, closed, variation + "(")

        if closed < open:
            backtrack(open, closed + 1, variation + ")")

    backtrack(0, 0, "")
    return res


solution(3)
