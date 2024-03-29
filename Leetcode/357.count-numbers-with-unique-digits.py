#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# Given an integer n, return the count of all numbers with unique digits, x,
# where 0 <= x < 10^n.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, excluding 11,22,33,44,55,66,77,88,99
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= n <= 8
#
#
#


# 3/9 cases passed (N/A)
# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def repeatingNum(n):
            nStr = str(n)
            initial = nStr[0]
            for c in range(1,len(nStr) - 1):
                if nStr[c] == initial:
                    return True
            return False

        res = 0
        for n in range(pow(10, n)):
            if len(str(n)) > 1 and repeatingNum(n):
                continue
            else:
                res += 1
        return res


# @lc code=end

print(Solution().countNumbersWithUniqueDigits(3))
