#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# Key:
# Sliding window


# # Time: O(n), Space: O(n)


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        validator = set()
        l = 0
        res = 0

        for r in s:
            while r in validator:
                validator.remove(s[l])
                l += 1

            validator.add(r)
            res = max(res, len(validator))

        return res


# @lc code=end


def lengthOfLongestSubstring(s):
    # validates unique strings
    validator = set()
    left = 0
    res = 0

    # right variable will constantly moving right
    for right in s:
        # if the right char is in validator set
        # *** important ***
        # say is the window is [a, b, c] and the next chat is b
        # this while loop and left += 1 will keep running and remove "a" and "b" from our window
        while right in validator:
            # remove the very first element which is the repeating char
            validator.remove(s[left])
            left += 1
        # keep adding the right character and update the result with the bigger number
        # comparing current result and current length of the validator set
        validator.add(right)
        res = max(res, len(validator))

    return res


s = "dvdf"
lengthOfLongestSubstring(s)
