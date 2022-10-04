def generateParenthesis(n):
    res = []

    def backtracking(leftN, rightN, path):
        # result and append
        if leftN == n and rightN == n:
            res.append(path)

        # if left is higher than right we can add a right
        if leftN > rightN:
            backtracking(leftN, rightN + 1, path + ")")

        if leftN < n:
            backtracking(leftN + 1, rightN, path + "(")

    backtracking(0, 0, "")

    print(res)
    return res


generateParenthesis(3)
