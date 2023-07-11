from typing import *
import os
os.system('clear')


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            for j in range(len(res[-1]) + 1):
                l, r = 0, 1
                curr = []
                while r < len(temp):
                    curr.append(temp[l] + temp[r])
                    l += 1
                    r += 1

            res.append(curr)

        return res


Solution.generate(1, 5)
