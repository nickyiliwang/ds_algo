from typing import List


class Solution:
    def nonDup(self, nums: List) -> List[List[str]]:
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())

            for j in range(i, len(nums)):
                dfs(i + 1, subset + [nums[j]])

        dfs([], 0)
        return res

    def withDup(self, nums: List) -> List[List[str]]:
        res = []

        def dfs(i, subset):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    dfs(i + 1, subset + [nums[j]])

        dfs([], 0)
        return res
