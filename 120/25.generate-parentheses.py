#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#
from typing import List
# Key:
# In the backtracking fn, start with open bracket if open is less than n
# close when closed is less than open

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =  []
        
        def backtracking(open, closed, paren):
            if open == closed == n:
                res.append(paren)

            if open < n:
                backtracking(open + 1, closed, paren + "(")

            if closed < open:
                backtracking(open, closed + 1, paren + ")")

        backtracking(0, 0, "")    

        return res

        
# @lc code=end

print(
    Solution().generateParenthesis(3)
    
)
