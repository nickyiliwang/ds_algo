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

# Explanation
# Doing this we can go from O(n ^ 3) to calculate every sub array's max sum

# But doing this we can ignore any current sum that results in a negative number. the first number as the result will help filter out any current number that's not bigger than result. (using max)

print(
    Solution.maxSubArray(1, [5, 4, -1, 7, 8])
)
