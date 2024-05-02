#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1
# 
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#
# Key
# Shifting window
# 1) establish a window and add one letter and remove one letter

from collections import Counter

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter()
        window = len(s1)
        
        for i in range(len(s2)):
            if i < window:
                c2[s2[i]] += 1
            else:
                c2[s2[i - window]] -= 1
                c2[s2[i]] += 1
                     
            if c1 == c2:
                return True
        
        return False


        
# @lc code=end

