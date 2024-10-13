#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (53.99%)
# Likes:    9424
# Dislikes: 977
# Total Accepted:    1.5M
# Total Submissions: 2.8M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#

# 0 + 0 = 0
# 1 + 0 = 1
# 1 + 1 = 0 (carry 1)
# 1 + 1 + (carry 1) = 1 (carry 1)

# bin(3)
# '0b11'
# bin(-10)
# '-0b1010'

# int(num, base)


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).replace("0b", "")


# @lc code=end

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         res = []
#         carry = 0
#         i, j = len(a) - 1, len(b) - 1

#         while i >= 0 or j >= 0 or carry:
#             if i >= 0:
#                 carry += int(a[i])
#                 i -= 1
#             if j >= 0:
#                 carry += int(b[j])
#                 j -= 1
#             res.append(str(carry % 2))
#             carry //= 2

#         return "".join(reversed(res))
