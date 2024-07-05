#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#
from collections import Counter

# Key:
# while (r - l + 1) - max(counter.values()) > k:
# k is the char limit, while we have replaced more char than this limit, we need to move the left pointer
# (r - l + 1) == the len of the window, this minus the largest num in the counter gets how many char was replaced
# interestingly, we don't need to know which numbers are replaced
# sliding window
# O(n) time and space

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l = 0, 0
        counter = Counter()
        
        for r in range(len(s)):
            counter[s[r]] += 1
            
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))     
        
        return res    
# @lc code=end

