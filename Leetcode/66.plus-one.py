#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (44.22%)
# Likes:    8687
# Dislikes: 5276
# Total Accepted:    2M
# Total Submissions: 4.5M
# Testcase Example:  '[1,2,3]'
#
# You are given a large integer represented as an integer array digits, where
# each digits[i] is the i^th digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of
# digits.
# 
# 
# Example 1:
# 
# 
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# 
# 
# Example 2:
# 
# 
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# 
# 
# Example 3:
# 
# 
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
# 
# 
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        combined_num = ''.join(str(num) for num in digits)

        combined_num = int(combined_num)
        combined_num += 1
        
        
        print(type(combined_num))
        
        # digits = [int(n) for n in combined_num]
        # print(digits)
        # return digits



Solution.plusOne("", [1,2,9])
        
# @lc code=end

