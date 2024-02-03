#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#
# https://leetcode.com/problems/merge-strings-alternately/description/
#
# algorithms
# Easy (79.31%)
# Likes:    3493
# Dislikes: 72
# Total Accepted:    623.3K
# Total Submissions: 785.5K
# Testcase Example:  '"abc"\n"pqr"'
#
# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer than
# the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
# Example 1:
#
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
#
# Example 2:
#
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
#
#
# Example 3:
#
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
#
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left, right = 0, 0
        loops = min(len(word1), len(word2))
        res = ""

        while loops:
            res += word1[left]
            res += word2[right]
            left += 1
            right += 1
            loops -= 1

        return res + word1[left:] + word2[right:]


# @lc code=end
solution = Solution()

print(solution.mergeAlternately("ab", "pqrs"))
