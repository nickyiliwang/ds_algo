#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (41.78%)
# Likes:    6974
# Dislikes: 919
# Total Accepted:    633K
# Total Submissions: 1.5M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#


# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        wordToPattern = {}
        patternToWord = {}
        if len(words) != len(pattern):
            return False
        
        if len(set(words)) != len(set(pattern)):
            return False

        for p, w in zip(pattern, words):
            if p in patternToWord and patternToWord[p] != w:
                return False
            if w in wordToPattern and wordToPattern[w] != p:
                return False
            
            wordToPattern[w] = p
            patternToWord[p] = w

        return True


# @lc code=end

print(Solution.wordPattern("", "abba", "cat dog dog cat"))
