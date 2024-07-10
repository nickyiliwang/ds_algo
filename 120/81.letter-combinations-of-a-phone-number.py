#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#

from typing import List


# @lc code=start
# O(n4 ^ n) ie. 99999
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, str):
            if i == len(digits):
                res.append(str)
                return

            for char in digDict[digits[i]]:
                backtrack(i + 1, str + char)

        if digits:
            backtrack(0, "")

        return res


# @lc code=end

print(
    Solution().letterCombinations("23")
    # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
)
