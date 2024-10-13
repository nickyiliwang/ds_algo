#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (82.69%)
# Likes:    5029
# Dislikes: 349
# Total Accepted:    183.6K
# Total Submissions: 222.1K
# Testcase Example:  '7'
#
# Given an integer n, return a list of all possible full binary trees with n
# nodes. Each node of each tree in the answer must have Node.val == 0.
# 
# Each element of the answer is the root node of one possible tree. You may
# return the final list of trees in any order.
# 
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# 
# Example 1:
# 
# 
# Input: n = 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: [[0,0,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # list of bt with n nodes
        def dfs(n):
            if n == 0:
                return []
                
            if n == 1:
                return [TreeNode()]    
            
            res = []
            for l in range(n): #  0 - (n - 1)
                r = n - 1 - l
                
                leftTrees, rightTrees = dfs(l), dfs(r)
            
            
            
                

        
        
        
# @lc code=end

