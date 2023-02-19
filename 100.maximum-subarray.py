from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0

        for num in nums:
            if curr < 0:
                curr = 0

        curr += num

        res = max(res, curr)

        return res


print(
    Solution.maxSubArray(1, [5, 4, -1, 7, 8])
)
