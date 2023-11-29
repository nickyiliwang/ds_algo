#
# @lc app=leetcode id=2423 lang=python3
#
# [2423] Remove Letter To Equalize Frequency
#
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/
#
# algorithms
# Easy (17.36%)
# Likes:    581
# Dislikes: 1112
# Total Accepted:    35.8K
# Total Submissions: 207.6K
# Testcase Example:  '"abcc"'
#
# You are given a 0-indexed string word, consisting of lowercase English
# letters. You need to select one index and remove the letter at that index
# from word so that the frequency of every letter present in word is equal.
#
# Return true if it is possible to remove one letter so that the frequency of
# all letters in word are equal, and false otherwise.
#
# Note:
#
#
# The frequency of a letter x is the number of times it occurs in the
# string.
# You must remove exactly one letter and cannot choose to do nothing.
#
#
#
# Example 1:
#
#
# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each
# character has a frequency of 1.
#
#
# Example 2:
#
#
# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1
# and the frequency of "z" is 2, or vice versa. It is impossible to make all
# present letters have equal frequency.
#
#
#
# Constraints:
#
#
# 2 <= word.length <= 100
# word consists of lowercase English letters only.
#
#
#

# @lc code=start

# My solution, does not resolve "bac"
from collections import Counter

# Cool solution

# We are taking off 1 for each letter from the counter, and checking to see if we can find an instance of everything being equal


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for char in word:
            counter[char] -= 1  # <= Take off 1
            if counter[char] == 0:
                counter.pop(char)

            if (len(set(counter.values())) == 1):
                return True
            counter[char] += 1  # <= Add back 1
        return False

# # My solution, does not resolve "bac"
# # 37 / 49 testcases passed
# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         hash = dict()
#         max_char_count = 0
#         max_char = ""

#         for char in word:
#             hash[char] = hash.get(char, 0) + 1
#             if (hash[char] > max_char_count):
#                 max_char = char
#                 max_char_count = hash[char]


#         hash[max_char] = hash[max_char] - 1
#         if (len(set(hash.values())) == 1):
#             return True
#         return False
Solution.equalFrequency("", "aazz")
# @lc code=end
