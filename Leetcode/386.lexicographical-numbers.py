#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (63.45%)
# Likes:    1913
# Dislikes: 140
# Total Accepted:    116.8K
# Total Submissions: 184K
# Testcase Example:  '13'
#
# Given an integer n, return all the numbers in the range [1, n] sorted in
# lexicographical order.
# 
# You must write an algorithm that runs in O(n) time and uses O(1) extra
# space. 
# 
# 
# Example 1:
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:
# Input: n = 2
# Output: [1,2]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 5 * 10^4
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
# @lc code=end

