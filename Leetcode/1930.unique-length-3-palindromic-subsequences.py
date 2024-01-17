#
# @lc app=leetcode id=1930 lang=python
#
# [1930] Unique Length-3 Palindromic Subsequences
#
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
#
# algorithms
# Medium (66.10%)
# Likes:    1670
# Dislikes: 68
# Total Accepted:    98.1K
# Total Submissions: 148.4K
# Testcase Example:  '"aabca"'
#
# Given a string s, return the number of unique palindromes of length three
# that are a subsequence of s.
#
# Note that even if there are multiple ways to obtain the same subsequence, it
# is still only counted once.
#
# A palindrome is a string that reads the same forwards and backwards.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
#
# Example 1:
#
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
#
#
# Example 2:
#
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
#
#
# Example 3:
#
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
#
# Constraints:
#
#
# 3 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#
#


# @lc code=start
class Solution(object):
    def countPalindromicSubsequence(self, s):
        count = 0
        chars = set(s)

        for char in chars:
            left, right = s.find(char), s.rfind(char)
            count += len(set(s[left + 1 : right]))

        return count


# @lc code=end

# left, right = s.find(char), s.rfind(char): This line finds the first occurrence (left) and the last occurrence (right) of the current character char in the string s. The find() method returns the index of the first occurrence of the character, while the rfind() method returns the index of the last occurrence.

# count += len(set(s[left + 1 : right])): This line increments the count variable by the length of the set of characters between the first and last occurrences of char in the string s. The set() function is used to remove any duplicate characters in this substring.

# why the left + 1 ?

# The left + 1 is used in the line count += len(set(s[left + 1 : right])) to exclude the first occurrence of the character char from the substring that is being considered.

# Here's why:

# When finding the first occurrence of char using s.find(char), it returns the index of the first occurrence. Let's say this index is left.

# In order to count the distinct characters between the first and last occurrences of char, we need to exclude the first occurrence itself. This is because we are interested in the characters that appear between the first and last occurrences, not including the first occurrence.

# So, by using left + 1 as the starting index in the substring s[left + 1 : right], we effectively exclude the first occurrence of char from the substring.

# This ensures that we only consider the distinct characters between the first and last occurrences of char when counting the palindromic subsequences.
