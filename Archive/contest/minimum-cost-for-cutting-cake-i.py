from typing import *
from collections import *

# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/description/

# did not pass
class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        cuts = []
        for i in range(m - 1):
            cuts.append((horizontalCut[i], "horizontal"))
        for j in range(n - 1):
            cuts.append((verticalCut[j], "vertical"))

        cost_v_first = 0
        cost_h_first = 0

        for cost, cut_type in cuts:
            if cut_type == "horizontal":
                cost_v_first += cost * n
                cost_h_first += cost
            else:
                cost_v_first += cost
                cost_h_first += cost * m

        return min(cost_h_first, cost_v_first)


print(
    Solution().minimumCost(6, 3, [2,3,2,3,1], [1,2])
    # 28
)
